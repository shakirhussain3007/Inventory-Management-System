from pydantic import BaseModel, ConfigDict, Field


class LoginRequest(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50
    )

    password: str = Field(
        ...,
        min_length=8,
        max_length=100
    )


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

    model_config = ConfigDict(from_attributes=True)


class ChangeOwnPassword(BaseModel):
    current_password: str = Field(
        ...,
        min_length=8,
        max_length=100
    )

    new_password: str = Field(
        ...,
        min_length=8,
        max_length=100
    )


class ChangeStaffPassword(BaseModel):
    user_id: int

    new_password: str = Field(
        ...,
        min_length=8,
        max_length=100
    )