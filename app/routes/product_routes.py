from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.config.dependencies import (
    get_db,
    get_current_admin,
    get_current_staff_or_admin
)

from app.models.user import User

from app.schemas.product_schema import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
)

from app.controllers.product_controller import (
    create_product_controller,
    get_all_products_controller,
    get_product_by_id_controller,
    update_product_controller,
    delete_product_controller,
    search_product_controller,
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post(
    "/",
    response_model=ProductResponse,
    status_code=201
)
def create_product(
    product_data: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    return create_product_controller(
        db,
        product_data
    )


@router.get(
    "/",
    response_model=list[ProductResponse]
)
def get_all_products(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_staff_or_admin)
):
    return get_all_products_controller(db)


@router.get(
    "/search",
    response_model=list[ProductResponse]
)
def search_product(
    keyword: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_staff_or_admin)
):
    return search_product_controller(
        db,
        keyword
    )


@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get_product_by_id(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_staff_or_admin)
):
    return get_product_by_id_controller(
        db,
        product_id
    )


@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def update_product(
    product_id: int,
    product_data: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    return update_product_controller(
        db,
        product_id,
        product_data
    )


@router.delete(
    "/{product_id}"
)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_admin)
):
    return delete_product_controller(
        db,
        product_id
    )