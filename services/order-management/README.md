# Order Management Service

Implementation of the Order Management domain capability for the ecommerce domain (tmfc001).

## Owning Domain
[Ecommerce Domain](../../DOMAIN.md)

## Capabilities
- Manages customer orders from creation through fulfillment
- Implements TMF622 Product Order Management API
- Supports order status updates, cancellation, and lifecycle management

## Implementation Details
- **Domain Aggregate**: CustomerOrder (ent-customer-order)
- **Database**: PostgreSQL with JPA/Hibernate
- **TMF Alignment**: TMF622 Product Order Management
- **Patterns**: Saga orchestration for order fulfillment with compensating actions

## Architecture
See domain design for detailed specification:
[architecture/domains/ecommerce/domain-design.yml](../../architecture/domains/ecommerce/domain-design.yml)
[architecture/domains/ecommerce/component-specs.yml](../../architecture/domains/ecommerce/component-specs.yml)