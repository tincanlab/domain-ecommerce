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
- **Database**: PostgreSQL with JPA/Hibernate
- **TMF Alignment**: TMF620 Product Catalog Management

## Architecture
See domain design for detailed specification:
[architecture/domains/ecommerce/domain-design.yml](../../architecture/domains/ecommerce/domain-design.yml)
[architecture/domains/ecommerce/component-specs.yml](../../architecture/domains/ecommerce/component-specs.yml)