from sqlalchemy.orm import Session

from app.models.user import User

from app.schemas.admin_schema import (
    AdminProfileCreate,
    AdminProfileUpdate
)

from app.services.admin_service import (
    create_profile,
    get_profile,
    update_profile,
    remove_profile
)


def create_admin_profile_controller(
    db: Session,
    profile_data: AdminProfileCreate,
    current_user: User
):
    return create_profile(
        db,
        profile_data,
        current_user
    )


def get_admin_profile_controller(
    db: Session,
    current_user: User
):
    return get_profile(
        db,
        current_user
    )


def update_admin_profile_controller(
    db: Session,
    profile_data: AdminProfileUpdate,
    current_user: User
):
    return update_profile(
        db,
        profile_data,
        current_user
    )


def delete_admin_profile_controller(
    db: Session,
    current_user: User
):
    return remove_profile(
        db,
        current_user
    )