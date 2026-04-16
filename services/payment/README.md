# Payment Service

Implementation of the Payment domain capability for the ecommerce domain (tmfc001).

## Owning Domain
[Ecommerce Domain](../../DOMAIN.md)

## Capabilities
- Handles payment capture, authorization, and validation
- Implements TMF669 Payment API via TMFC009 ODA Component
- Supports refund processing (partial and full)
- Integrates with external payment gateways
- Provides transaction logging for audit compliance

## Implementation Details
- **Domain Aggregate**: Payment (ent-payment)
- **Database**: PostgreSQL with JPA/Hibernate
- **TMF Alignment**: TMF669 Payment, TMFC009 ODA Component
- **Patterns**: Idempotent payment processing, saga compensation for order-payment rollback

## Architecture
See domain design for detailed specification:
[architecture/domains/ecommerce/domain-design.yml](../../architecture/domains/ecommerce/domain-design.yml)
[architecture/domains/ecommerce/component-specs.yml](../../architecture/domains/ecommerce/component-specs.yml)