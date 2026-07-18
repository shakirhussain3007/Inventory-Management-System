from datetime import datetime, UTC

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.db import Base


class AdminProfile(Base):
    __tablename__ = "admin_profiles"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    owner_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    shop_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    shop_address: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )

    shop_phone: Mapped[str] = mapped_column(
        String(20),
        nullable=True
    )

    profile_picture: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )

    shop_logo: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC)
    )

    user = relationship("User")