from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProductOfferingBase(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    isBundle: Optional[bool] = False
    lifecycleStatus: Optional[str] = None
    version: Optional[str] = "1.0"

class ProductOfferingCreate(ProductOfferingBase):
    pass

class ProductOfferingUpdate(ProductOfferingBase):
    pass

class ProductOffering(ProductOfferingBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
