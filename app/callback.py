import requests
import os

def send_final_result(session_id, session):
    payload = {
        "sessionId": session_id,
        "scamDetected": True,
        "totalMessagesExchanged": len(session["messages"]),
        "extractedIntelligence": session["intelligence"],
        "agentNotes": "Urgency-based financial scam detected"
    }

    requests.post(
        os.getenv("GUVI_CALLBACK"),
        json=payload,
        timeout=5
    )
