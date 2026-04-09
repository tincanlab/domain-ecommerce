from fastapi import FastAPI
from app.api import health, product_offering
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Product Catalog Service",
    description="TMF620 Product Catalog Management API implementation",
    version="0.1.0"
)

# Include routers
app.include_router(health.router, tags=["health"])
app.include_router(product_offering.router, tags=["productOffering"])
