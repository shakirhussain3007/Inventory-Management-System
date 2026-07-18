from sqlalchemy.orm import Session

from app.schemas.product_schema import ProductCreate, ProductUpdate

from app.services.product_service import (
    create_new_product,
    get_products,
    get_single_product,
    update_existing_product,
    delete_existing_product,
    search_product,
)


def create_product_controller(
    db: Session,
    product_data: ProductCreate
):
    return create_new_product(db, product_data)


def get_all_products_controller(db: Session):
    return get_products(db)


def get_product_by_id_controller(
    db: Session,
    product_id: int
):
    return get_single_product(db, product_id)


def update_product_controller(
    db: Session,
    product_id: int,
    product_data: ProductUpdate
):
    return update_existing_product(
        db,
        product_id,
        product_data
    )


def delete_product_controller(
    db: Session,
    product_id: int
):
    return delete_existing_product(
        db,
        product_id
    )


def search_product_controller(
    db: Session,
    keyword: str
):
    return search_product(db, keyword)