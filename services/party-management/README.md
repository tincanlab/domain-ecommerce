# Party Management Service

Implementation of the Party Management domain capability for the ecommerce domain (tmfc001).

## Owning Domain
[Ecommerce Domain](../../DOMAIN.md)

## Capabilities
- Manages customer, partner, and third-party profiles
- Handles customer addresses, contact information, and preferences
- Supports consent management and profile enrichment
- Implements TMF622 Party Management via TMFC028 ODA Component

## Implementation Details
- **Domain Aggregate**: Party (ent-party)
- **Database**: PostgreSQL with JPA/Hibernate
- **TMF Alignment**: TMF622 Party Management, TMFC028 ODA Component
- **Patterns**: Address validation via external geocoding service

## Architecture
See domain design for detailed specification:
[architecture/domains/ecommerce/domain-design.yml](../../architecture/domains/ecommerce/domain-design.yml)
[architecture/domains/ecommerce/component-specs.yml](../../architecture/domains/ecommerce/component-specs.yml)