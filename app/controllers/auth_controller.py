from sqlalchemy.orm import Session

from app.services.auth_service import login_user


def login_controller(
    db: Session,
    username: str,
    password: str
):
    return login_user(
        db,
        username,
        password
    )