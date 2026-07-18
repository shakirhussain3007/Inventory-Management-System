from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.config.db import SessionLocal
from app.config.security import oauth2_scheme

from app.repositories.user_repo import get_user_by_id
from app.utils.jwt import verify_access_token

from app.models.user import User

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    payload = verify_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token."
        )

    user = get_user_by_id(
        db,
        payload["user_id"]
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found."
        )

    return user

def get_current_admin(
    current_user: User = Depends(get_current_user)
):
    if current_user.role != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Admin can access this resource."
        )

    return current_user


def get_current_staff_or_admin(
    current_user: User = Depends(get_current_user)
):
    if current_user.role not in [
        "ADMIN",
        "STAFF"
    ]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied."
        )

    return current_user