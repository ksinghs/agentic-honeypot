from fastapi import Header, HTTPException

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != "super-secret-key":
        raise HTTPException(status_code=401, detail="Invalid API key")
