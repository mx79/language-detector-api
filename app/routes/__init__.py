from functools import wraps
from hmac import compare_digest
from fastapi import HTTPException
from config import Config


def auth_required(func):
    @wraps(func)
    async def wrapper(request, *args, **kwargs):
        x_api_key = request.headers.get("X-API-KEY")
        if x_api_key is None:
            raise HTTPException(status_code=400, detail="Malformed request")
        if compare_digest(x_api_key, Config.X_API_KEY):
            return await func(*args, request, **kwargs)
        else:
            raise HTTPException(status_code=401, detail="Invalid client secret")

    return wrapper
