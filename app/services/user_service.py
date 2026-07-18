from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user import User
from app.schemas.user_schema import UserCreate, UserUpdate

from app.repositories.user_repo import (
    create_user,
    get_all_users,
    get_user_by_id,
    get_user_by_username,
    update_user,
    delete_user,
)

from app.utils.hash import hash_password


def create_new_user(db: Session, user_data: UserCreate):

    existing_user = get_user_by_username(db, user_data.username)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists."
        )

    new_user = User(
        username=user_data.username,
        password=hash_password(user_data.password),
        role=user_data.role
    )

    return create_user(db, new_user)


def get_users(db: Session):
    return get_all_users(db)


def get_single_user(db: Session, user_id: int):

    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )

    return user


def update_existing_user(
    db: Session,
    user_id: int,
    user_data: UserUpdate
):

    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )

    user.username = user_data.username
    user.role = user_data.role

    return update_user(db, user)


def delete_existing_user(
    db: Session,
    user_id: int
):

    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )

    delete_user(db, user)

    return {
        "message": "User deleted successfully."
    }