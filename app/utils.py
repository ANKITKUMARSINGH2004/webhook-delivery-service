import hmac
import hashlib
import base64
from fastapi import HTTPException

def verify_signature(secret: str, payload: dict):
    """Verifies HMAC SHA256 signature if secret is provided."""
    if not secret:
        return

    signature_header = payload.get('signature')
    if not signature_header:
        raise HTTPException(status_code=400, detail="Missing signature in payload")

    body = payload.get('body')
    if body is None:
        raise HTTPException(status_code=400, detail="Missing body in payload")

    computed_signature = hmac.new(
        secret.encode(),
        body.encode(),
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(signature_header, computed_signature):
        raise HTTPException(status_code=403, detail="Invalid signature")
