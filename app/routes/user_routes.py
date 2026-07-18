from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.dependencies import (
    get_db,
    get_current_admin
)

from app.models.user import User

from app.schemas.user_schema import (
    UserCreate,
    UserUpdate,
    UserResponse,
)

from app.controllers.user_controller import (
    create_user_controller,
    get_all_users_controller,
    get_user_by_id_controller,
    update_user_controller,
    delete_user_controller,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=201
)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    return create_user_controller(
        db,
        user_data
    )


@router.get(
    "/",
    response_model=list[UserResponse]
)
def get_all_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    return get_all_users_controller(db)


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    return get_user_by_id_controller(
        db,
        user_id
    )


@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    return update_user_controller(
        db,
        user_id,
        user_data
    )


@router.delete(
    "/{user_id}"
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    return delete_user_controller(
        db,
        user_id
    )