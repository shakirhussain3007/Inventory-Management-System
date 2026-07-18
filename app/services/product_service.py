from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.product import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate

from app.repositories.product_repo import (
    create_product,
    get_all_products,
    get_product_by_id,
    search_products,
    update_product,
    delete_product,
)


def create_new_product(db: Session, product_data: ProductCreate):

    new_product = Product(
        name=product_data.name,
        description=product_data.description,
        category=product_data.category,
        price=product_data.price,
        quantity=product_data.quantity
    )

    return create_product(db, new_product)


def get_products(db: Session):
    return get_all_products(db)


def get_single_product(db: Session, product_id: int):

    product = get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found."
        )

    return product


def update_existing_product(
    db: Session,
    product_id: int,
    product_data: ProductUpdate
):

    product = get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found."
        )

    product.name = product_data.name
    product.description = product_data.description
    product.category = product_data.category
    product.price = product_data.price
    product.quantity = product_data.quantity

    return update_product(db, product)


def delete_existing_product(
    db: Session,
    product_id: int
):

    product = get_product_by_id(db, product_id)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found."
        )

    delete_product(db, product)

    return {
        "message": "Product deleted successfully."
    }


def search_product(db: Session, keyword: str):
    return search_products(db, keyword)