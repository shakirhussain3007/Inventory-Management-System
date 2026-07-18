from pydantic import BaseModel, ConfigDict, Field
from typing import Literal


class UserCreate(BaseModel):
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

    role: Literal["ADMIN", "STAFF"]


class UserUpdate(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50
    )

    role: Literal["ADMIN", "STAFF"]


class UserResponse(BaseModel):
    id: int
    username: str
    role: str

    model_config = ConfigDict(from_attributes=True)