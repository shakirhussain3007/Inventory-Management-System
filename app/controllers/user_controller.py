from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate, UserUpdate

from app.services.user_service import (
    create_new_user,
    get_users,
    get_single_user,
    update_existing_user,
    delete_existing_user,
)


def create_user_controller(
    db: Session,
    user_data: UserCreate
):
    return create_new_user(db, user_data)


def get_all_users_controller(
    db: Session
):
    return get_users(db)


def get_user_by_id_controller(
    db: Session,
    user_id: int
):
    return get_single_user(db, user_id)


def update_user_controller(
    db: Session,
    user_id: int,
    user_data: UserUpdate
):
    return update_existing_user(
        db,
        user_id,
        user_data
    )


def delete_user_controller(
    db: Session,
    user_id: int
):
    return delete_existing_user(
        db,
        user_id
    )