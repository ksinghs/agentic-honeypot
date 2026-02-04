from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from dotenv import load_dotenv
import os

from app.session import SessionStore
from app.detector import HoneypotDetector
from app.agent import LLMAgent
from app.intelligence import EvidenceLogger
from app.detector import GeoResolver
from app.callback import GuviNotifier

load_dotenv()

API_KEY = os.getenv("HONEY_API_KEY")
RATE_LIMIT = "5/minute"

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="Agentic Honeypot API")
app.state.limiter = limiter

session_store = SessionStore(ttl_seconds=300)
detector = HoneypotDetector()
agent = LLMAgent()
logger = EvidenceLogger()
geo = GeoResolver()
guvi = GuviNotifier()


@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request, exc):
    return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})


@app.post("/honeypot")
@limiter.limit(RATE_LIMIT)
async def honeypot(request: Request, x_api_key: str = Header(None)):
    ip = request.client.host
    payload = await request.json()

    if x_api_key != API_KEY:
        logger.log_event(ip, "AUTH_FAIL", payload)
        raise HTTPException(status_code=401, detail="Invalid API key")

    session_id = session_store.create_or_refresh(ip)
    detection = detector.analyze(payload)
    fingerprint = detector.fingerprint(payload)
    geo_info = geo.resolve(ip)
    agent_reply = agent.respond(payload, detection)

    event = {
        "session_id": session_id,
        "payload": payload,
        "analysis": detection,
        "fingerprint": fingerprint,
        "geo": geo_info,
        "agent_reply": agent_reply,
    }

    logger.log_event(ip, "HONEYPOT_HIT", event)

    if detection["suspicious"]:
        guvi.notify(event)

    return {
        "status": "ok",
        "session_id": session_id,
        "analysis": detection,
        "fingerprint": fingerprint,
        "agent_reply": agent_reply,
    }
