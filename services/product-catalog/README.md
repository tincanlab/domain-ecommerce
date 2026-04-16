# Product Catalog Service

Implementation of the Product Catalog domain capability for the ecommerce domain (tmfc001).

## Owning Domain
[Ecommerce Domain](../../DOMAIN.md)

## Capabilities
- Manages product definitions, pricing, and categorization
- Implements TMF620 Product Catalog Management API
- Supports product search, browsing, and lifecycle management

## Implementation Details
- **Domain Aggregate**: ProductCatalog (ent-product-catalog)
- **Framework**: FastAPI (Python)
- **Database**: SQLite (development), can be configured for PostgreSQL
- **TMF Alignment**: TMF620 Product Catalog Management

## Architecture
See domain design for detailed specification:
[architecture/domains/ecommerce/domain-design.yml](../../architecture/domains/ecommerce/domain-design.yml)
[architecture/domains/ecommerce/component-specs.yml](../../architecture/domains/ecommerce/component-specs.yml)

## Running Locally

1. Install dependencies:
```bash
cd services/product-catalog
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn app.main:app --reload
```

3. The service will be available at http://localhost:8000
   - Health checks: http://localhost:8000/health/liveness, http://localhost:8000/health/readiness
   - API docs: http://localhost:8000/docs
   - Product Offering endpoints: GET/POST/PATCH/DELETE `/productOffering/{id}`

4. Run tests:
```bash
pytest tests/ -v
```