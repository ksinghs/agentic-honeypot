import hashlib
import json

class HoneypotDetector:
    def analyze(self, payload: dict):
        suspicious = ["cmd", "exec", "drop", "password", "token"]
        score = sum(1 for k in payload if k.lower() in suspicious)

        return {
            "suspicious": score > 0,
            "score": score,
            "type": "command_injection" if score else "benign"
        }

    def fingerprint(self, payload: dict):
        raw = json.dumps(payload, sort_keys=True)
        return {
            "hash": hashlib.sha256(raw.encode()).hexdigest(),
            "size": len(raw),
            "keys": list(payload.keys())
        }
