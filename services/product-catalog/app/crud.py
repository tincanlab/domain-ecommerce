from sqlalchemy.orm import Session
from app.models import ProductOffering
from app.schemas import ProductOfferingCreate, ProductOfferingUpdate
from typing import List, Optional

def get_product_offering(db: Session, product_id: str) -> Optional[ProductOffering]:
    return db.query(ProductOffering).filter(ProductOffering.id == product_id).first()

def get_product_offerings(db: Session, skip: int = 0, limit: int = 10) -> List[ProductOffering]:
    return db.query(ProductOffering).offset(skip).limit(limit).all()

def create_product_offering(db: Session, product: ProductOfferingCreate) -> ProductOffering:
    db_product = ProductOffering(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product_offering(db: Session, product_id: str, product_update: ProductOfferingUpdate) -> Optional[ProductOffering]:
    db_product = get_product_offering(db, product_id)
    if db_product:
        for key, value in product_update.dict(exclude_unset=True).items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product_offering(db: Session, product_id: str) -> bool:
    db_product = get_product_offering(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
        return True
    return False
