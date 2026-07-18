from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class ProductCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    description: str | None = Field(
        default=None,
        max_length=500
    )

    category: str = Field(
        ...,
        min_length=2,
        max_length=50
    )

    price: Decimal = Field(
        ...,
        gt=0
    )

    quantity: int = Field(
        ...,
        ge=0
    )


class ProductUpdate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    description: str | None = Field(
        default=None,
        max_length=500
    )

    category: str = Field(
        ...,
        min_length=2,
        max_length=50
    )

    price: Decimal = Field(
        ...,
        gt=0
    )

    quantity: int = Field(
        ...,
        ge=0
    )


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    category: str
    price: Decimal
    quantity: int

    model_config = ConfigDict(from_attributes=True)