# BOPIS Fulfillment Service

Implementation of the BOPIS (Buy Online, Pick Up In-Store) fulfillment capability for the ecommerce domain (tmfc001).

## Owning Domain
[Ecommerce Domain](../../DOMAIN.md)

## Capabilities
- Manages pickup slot reservations and store coordination
- Extends TMF622 Product Order Management with BOPIS-specific capabilities
- Handles pickup slot availability checking and capacity management
- Supports pickup confirmation and completion notification

## Implementation Details
- **Domain Aggregate**: CustomerOrder (ent-customer-order)
- **Database**: PostgreSQL with JPA/Hibernate
- **TMF Alignment**: TMF622 Product Order Management, TMFC003 ODA Component
- **Patterns**: Slot expiration with automatic release, optimistic locking for capacity management

## Architecture
See domain design for detailed specification:
[architecture/domains/ecommerce/domain-design.yml](../../architecture/domains/ecommerce/domain-design.yml)
[architecture/domains/ecommerce/component-specs.yml](../../architecture/domains/ecommerce/component-specs.yml)