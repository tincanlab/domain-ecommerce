from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/productOffering")

@router.get("/", response_model=List[schemas.ProductOffering])
def read_product_offerings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = crud.get_product_offerings(db, skip=skip, limit=limit)
    return products

@router.get("/{product_id}", response_model=schemas.ProductOffering)
def read_product_offering(product_id: str, db: Session = Depends(get_db)):
    db_product = crud.get_product_offering(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product offering not found")
    return db_product

@router.post("/", response_model=schemas.ProductOffering, status_code=201)
def create_product_offering(product: schemas.ProductOfferingCreate, db: Session = Depends(get_db)):
    return crud.create_product_offering(db=db, product=product)

@router.patch("/{product_id}", response_model=schemas.ProductOffering)
def update_product_offering(product_id: str, product_update: schemas.ProductOfferingUpdate, db: Session = Depends(get_db)):
    db_product = crud.update_product_offering(db, product_id, product_update)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product offering not found")
    return db_product

@router.delete("/{product_id}", status_code=204)
def delete_product_offering(product_id: str, db: Session = Depends(get_db)):
    success = crud.delete_product_offering(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product offering not found")
