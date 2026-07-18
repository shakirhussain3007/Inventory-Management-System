from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.dependencies import (
    get_db,
    get_current_user,
    get_current_admin
)

from app.models.user import User

from app.schemas.admin_schema import (
    AdminProfileCreate,
    AdminProfileUpdate,
    AdminProfileResponse
)

from app.controllers.admin_controller import (
    create_admin_profile_controller,
    get_admin_profile_controller,
    update_admin_profile_controller,
    delete_admin_profile_controller
)

router = APIRouter(
    prefix="/admin",
    tags=["Admin Profile"]
)


@router.post(
    "/profile",
    response_model=AdminProfileResponse,
    status_code=201
)
def create_profile(
    profile_data: AdminProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    return create_admin_profile_controller(
        db,
        profile_data,
        current_user
    )


@router.get(
    "/profile/me",
    response_model=AdminProfileResponse
)
def get_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    return get_admin_profile_controller(
        db,
        current_user
    )


@router.put(
    "/profile/me",
    response_model=AdminProfileResponse
)
def update_profile(
    profile_data: AdminProfileUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    return update_admin_profile_controller(
        db,
        profile_data,
        current_user
    )


@router.delete("/profile/me")
def delete_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    return delete_admin_profile_controller(
        db,
        current_user
    )