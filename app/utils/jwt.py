from datetime import datetime, timedelta, UTC

from jose import jwt, JWTError

from app.config.settings import settings


def create_access_token(data: dict):
    """
    Generate JWT Access Token
    """

    payload = data.copy()

    expire = datetime.now(UTC) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update(
        {
            "exp": expire
        }
    )

    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return token


def verify_access_token(token: str):
    """
    Verify JWT Token
    """

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        return payload

    except JWTError:
        return None