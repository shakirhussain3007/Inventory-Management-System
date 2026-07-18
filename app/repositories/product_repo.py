from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.product import Product


def create_product(db: Session, product: Product):
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def get_all_products(db: Session):
    return db.query(Product).all()


def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def search_products(db: Session, keyword: str):
    return (
        db.query(Product)
        .filter(
            or_(
                Product.name.ilike(f"%{keyword}%"),
                Product.category.ilike(f"%{keyword}%")
            )
        )
        .all()
    )


def update_product(db: Session, product: Product):
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product: Product):
    db.delete(product)
    db.commit()