from pydantic import BaseModel, ConfigDict, Field


class AdminProfileCreate(BaseModel):
    owner_name: str = Field(
        ...,
        min_length=3,
        max_length=100
    )

    shop_name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    shop_address: str | None = Field(
        default=None,
        max_length=255
    )

    shop_phone: str | None = Field(
        default=None,
        max_length=20
    )

    profile_picture: str | None = None

    shop_logo: str | None = None


class AdminProfileUpdate(BaseModel):
    owner_name: str = Field(
        ...,
        min_length=3,
        max_length=100
    )

    shop_name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    shop_address: str | None = Field(
        default=None,
        max_length=255
    )

    shop_phone: str | None = Field(
        default=None,
        max_length=20
    )

    profile_picture: str | None = None

    shop_logo: str | None = None


class AdminProfileResponse(BaseModel):
    id: int
    owner_name: str
    shop_name: str
    shop_address: str | None
    shop_phone: str | None
    profile_picture: str | None
    shop_logo: str | None

    model_config = ConfigDict(
        from_attributes=True
    )