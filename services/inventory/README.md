# Inventory Service

Implementation of the Inventory Management domain capability for the ecommerce domain (tmfc001).

## Owning Domain
[Ecommerce Domain](../../DOMAIN.md)

## Capabilities
- Manages inventory levels across stores and warehouses
- Implements TMF637 Product Inventory Management API
- Supports inventory reservation, allocation, and adjustment
- Handles real-time availability checks

## Implementation Details
- **Domain Aggregate**: StoreInventory (ent-store-inventory)
- **Database**: PostgreSQL with JPA/Hibernate
- **TMF Alignment**: TMF637 Product Inventory Management
- **Patterns**: Inventory allocation strategy (store-first, warehouse-fallback), eventual consistency

## Architecture
See domain design for detailed specification:
[architecture/domains/ecommerce/domain-design.yml](../../architecture/domains/ecommerce/domain-design.yml)
[architecture/domains/ecommerce/component-specs.yml](../../architecture/domains/ecommerce/component-specs.yml)