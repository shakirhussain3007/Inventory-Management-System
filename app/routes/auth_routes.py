from app.config.dependencies import get_current_user
from app.models.user import User
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.dependencies import get_db

from app.schemas.auth_schema import (
    LoginRequest,
    TokenResponse
)

from app.controllers.auth_controller import (
    login_controller
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login_controller(
        db,
        form_data.username,
        form_data.password
    )
@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user