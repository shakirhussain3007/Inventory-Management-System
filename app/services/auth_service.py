from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.auth_schema import LoginRequest
from app.repositories.user_repo import get_user_by_username

from app.utils.hash import verify_password
from app.utils.jwt import create_access_token


def login_user(
    db: Session,
    username: str,
    password: str
):

    user = get_user_by_username(
    db,
    username
)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password."
        )

    if not verify_password(
    password,
    user.password
):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password."
        )

    access_token = create_access_token(
        {
            "user_id": user.id,
            "username": user.username,
            "role": user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }