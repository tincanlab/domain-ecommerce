from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base

class ProductOffering(Base):
    __tablename__ = "product_offering"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    isBundle = Column(Boolean, default=False)
    lifecycleStatus = Column(String, nullable=True)
    version = Column(String, default="1.0")
    validFor = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
