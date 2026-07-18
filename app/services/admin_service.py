from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.admin import AdminProfile
from app.models.user import User

from app.schemas.admin_schema import (
    AdminProfileCreate,
    AdminProfileUpdate
)

from app.repositories.admin_repo import (
    create_admin_profile,
    get_admin_profile_by_user_id,
    update_admin_profile,
    delete_admin_profile
)


def create_profile(
    db: Session,
    profile_data: AdminProfileCreate,
    current_user: User
):
    existing_profile = get_admin_profile_by_user_id(
        db,
        current_user.id
    )

    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Admin profile already exists."
        )

    profile = AdminProfile(
        user_id=current_user.id,
        owner_name=profile_data.owner_name,
        shop_name=profile_data.shop_name,
        shop_address=profile_data.shop_address,
        shop_phone=profile_data.shop_phone,
        profile_picture=profile_data.profile_picture,
        shop_logo=profile_data.shop_logo
    )

    return create_admin_profile(
        db,
        profile
    )


def get_profile(
    db: Session,
    current_user: User
):
    profile = get_admin_profile_by_user_id(
        db,
        current_user.id
    )

    if profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Admin profile not found."
        )

    return profile


def update_profile(
    db: Session,
    profile_data: AdminProfileUpdate,
    current_user: User
):
    profile = get_admin_profile_by_user_id(
        db,
        current_user.id
    )

    if profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Admin profile not found."
        )

    profile.owner_name = profile_data.owner_name
    profile.shop_name = profile_data.shop_name
    profile.shop_address = profile_data.shop_address
    profile.shop_phone = profile_data.shop_phone
    profile.profile_picture = profile_data.profile_picture
    profile.shop_logo = profile_data.shop_logo

    return update_admin_profile(
        db,
        profile
    )


def remove_profile(
    db: Session,
    current_user: User
):
    profile = get_admin_profile_by_user_id(
        db,
        current_user.id
    )

    if profile is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Admin profile not found."
        )

    delete_admin_profile(
        db,
        profile
    )

    return {
        "message": "Admin profile deleted successfully."
    }