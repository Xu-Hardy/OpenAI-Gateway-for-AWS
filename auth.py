from flask import request
from config import VALID_TOKENS

def verify_token(request):
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return False
    token = auth_header.split(" ")[1]
    return not token in VALID_TOKENS