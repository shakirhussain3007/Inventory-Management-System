from sqlalchemy.orm import Session

from app.models.admin import AdminProfile


def create_admin_profile(
    db: Session,
    profile: AdminProfile
):
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile


def get_admin_profile_by_user_id(
    db: Session,
    user_id: int
):
    return (
        db.query(AdminProfile)
        .filter(AdminProfile.user_id == user_id)
        .first()
    )


def update_admin_profile(
    db: Session,
    profile: AdminProfile
):
    db.commit()
    db.refresh(profile)
    return profile


def delete_admin_profile(
    db: Session,
    profile: AdminProfile
):
    db.delete(profile)
    db.commit()