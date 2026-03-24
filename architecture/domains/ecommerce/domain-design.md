# Domain Architecture: Ecommerce

## Context Evidence

- **Workspace**: ecommerce-domain
- **Domain**: ecommerce
- **Domain profile**: generic
- **SA baseline**: Direct domain initialization (no SA handoff)
- **Tools used**: domain-architecture skill
- **Generated**: 2026-03-22T22:47:00Z

## Domain Boundary

**Bounded context**: E-commerce domain covering online shopping, catalog management, order processing, and fulfillment capabilities including BOPIS (Buy Online, Pick Up In Store).

**Ubiquitous language**:
| Term | Definition |
|---|---|
| Product | An item available for purchase in the catalog |
| Order | A customer's request to purchase one or more products |
| Fulfillment | The process of preparing and delivering an order to the customer |
| BOPIS | Buy Online, Pick Up In Store - a fulfillment method where customers place orders online and collect them at a physical store |
| Inventory | Real-time stock levels across physical stores and warehouses |
| Pickup Slot | A reserved time window for BOPIS order collection |
| Store Location | Physical retail site where BOPIS orders are collected |

**Anti-corruption layers**:
- Inventory adapter to store management systems
- Payment gateway integration layer
- Shipping carrier adapter for non-BOPIS fulfillment

## Domain Model

### Core Aggregates

**Product Catalog Aggregate**
- Root: ProductCatalog
- Entities: Product, ProductCategory, ProductVariant
- Value Objects: Price, SKU, ProductAttributes

**Order Aggregate**
- Root: Order
- Entities: OrderItem, OrderFulfillment
- Value Objects: OrderStatus, PaymentDetails, FulfillmentMethod

**Inventory Aggregate**
- Root: Inventory
- Entities: StockLevel, InventoryReservation
- Value Objects: Location, StockStatus

**BOPIS Aggregate**
- Root: PickupSlot
- Entities: PickupReservation, StoreFulfillment
- Value Objects: PickupStatus, TimeWindow

### Key Relationships

- Product (1..*) → OrderItem
- Order (1..*) → OrderItem
- Order (1) → OrderFulfillment
- Inventory (1..*) → StockLevel per Location
- Order (1) → PickupSlot (if BOPIS)
- PickupSlot (1) → Store Location

### Domain Model Diagram

```mermaid
erDiagram
    ProductCatalog ||--o{ Product : contains
    ProductCatalog ||--o{ ProductCategory : categorizes
    Product ||--o{ OrderItem : included_in
    Product ||--o{ Inventory : tracked_at

    Order ||--o{ OrderItem : consists_of
    Order ||--|| OrderFulfillment : fulfilled_by
    Order ||--o| PickupSlot : "has (if BOPIS)"

    Inventory ||--o{ StockLevel : has
    Inventory }|--|| Store : located_at
    Inventory }|--|| Warehouse : located_at

    PickupSlot }|--|| Store : assigned_to

    Product {
        uuid id PK
        string name
        string sku UK
        decimal price
        string category_id FK
        enum status
    }

    Order {
        uuid id PK
        string customer_id FK
        datetime order_date
        enum fulfillment_method
        string fulfillment_store_id FK
        enum status
        decimal total_amount
    }

    OrderItem {
        uuid id PK
        uuid order_id FK
        uuid product_id FK
        integer quantity
        decimal unit_price
        decimal total_price
    }

    Inventory {
        uuid id PK
        uuid product_id FK
        uuid store_id FK
        uuid warehouse_id FK
        integer quantity_on_hand
        integer quantity_allocated
        integer quantity_available
    }

    PickupSlot {
        uuid id PK
        uuid order_id FK
        uuid store_id FK
        datetime start_time
        datetime end_time
        enum status
    }

    Store {
        uuid id PK
        string name
        string address
        enum status
    }
```

## Component Landscape

```mermaid
graph TB
    subgraph "Ecommerce Domain"
        subgraph "External Systems"
            StoreMgmtSys[Store Management System]
            PaymentGateway[Payment Gateway]
            ShippingCarrier[Shipping Carriers]
            NotificationSvc[Notification Service]
        end

        subgraph "Domain Services"
            ProductCatalogSvc[ProductCatalogService<br/>TMF620]
            OrderMgmtSvc[OrderManagementService<br/>TMF622]
            BOPISFulfillmentSvc[BOPISFulfillmentService]
            InventorySvc[InventoryService<br/>TMF637]
        end

        subgraph "Data Layer"
            ProductDB[(Product Catalog DB)]
            OrderDB[(Order DB)]
            InventoryDB[(Inventory DB)]
            PickupDB[(Pickup Slots DB)]
        end
    end

    ProductCatalogSvc -->|CRUD operations| ProductDB
    OrderMgmtSvc -->|Order lifecycle| OrderDB
    BOPISFulfillmentSvc -->|Slot management| PickupDB
    InventorySvc -->|Inventory tracking| InventoryDB

    OrderMgmtSvc -->|Product lookups| ProductCatalogSvc
    OrderMgmtSvc -->|Inventory check/reserve| InventorySvc
    OrderMgmtSvc -->|BOPIS coordination| BOPISFulfillmentSvc

    OrderMgmtSvc -->|Payment processing| PaymentGateway
    BOPISFulfillmentSvc -->|Store sync| StoreMgmtSys
    InventorySvc -->|Warehouse sync| StoreMgmtSys
    OrderMgmtSvc -->|Tracking updates| ShippingCarrier
    OrderMgmtSvc -->|Status notifications| NotificationSvc
    BOPISFulfillmentSvc -->|Pickup notifications| NotificationSvc

    style ProductCatalogSvc fill:#e1f5fe
    style OrderMgmtSvc fill:#e1f5fe
    style BOPISFulfillmentSvc fill:#fff3e0
    style InventorySvc fill:#e1f5fe
```

## Workflows

### BOPIS Order Fulfillment Workflow

```mermaid
sequenceDiagram
    participant C as Customer
    participant OMS as OrderManagementService
    participant IS as InventoryService
    participant BS as BOPISFulfillmentService
    participant SMS as StoreMgmtSys
    participant PG as PaymentGateway
    participant NS as NotificationSvc

    C->>OMS: Place Order (BOPIS fulfillment)
    OMS->>IS: Check inventory availability at store
    IS-->>OMS: Inventory available
    OMS->>PG: Process payment
    PG-->>OMS: Payment authorized

    OMS->>IS: Reserve inventory
    IS-->>OMS: Inventory reserved
    OMS->>BS: Assign pickup slot
    BS->>BS: Check slot availability
    BS-->>OMS: Pickup slot confirmed
    OMS->>NS: Send order confirmation

    OMS->>SMS: Notify store for fulfillment
    SMS-->>OMS: Fulfillment acknowledged
    OMS-->>C: Order confirmation with pickup details

    Note over BS: Order prepared at store
    BS->>NS: Notify pickup ready
    NS-->>C: Pickup ready notification

    C->>BS: Arrive for pickup
    BS->>BS: Verify pickup
    BS->>IS: Confirm pickup (decrement inventory)
    IS-->>BS: Inventory updated
    BS->>OMS: Complete order
    OMS->>NS: Send order completion
    NS-->>C: Order completed notification
```

### Standard Order Fulfillment Workflow

```mermaid
sequenceDiagram
    participant C as Customer
    participant OMS as OrderManagementService
    participant IS as InventoryService
    participant FC as FulfillmentCenter
    participant SC as ShippingCarrier
    participant PG as PaymentGateway
    participant NS as NotificationSvc

    C->>OMS: Place Order (shipping fulfillment)
    OMS->>IS: Check inventory availability at warehouse
    IS-->>OMS: Inventory available
    OMS->>PG: Process payment
    PG-->>OMS: Payment authorized

    OMS->>IS: Reserve inventory
    IS-->>OMS: Inventory reserved
    OMS->>FC: Route order to fulfillment center
    FC-->>OMS: Fulfillment accepted
    OMS->>NS: Send order confirmation
    NS-->>C: Order confirmation

    Note over FC: Pick, pack, and ship order
    FC->>SC: Hand off to shipping carrier
    SC-->>FC: Shipping label generated
    SC-->>OMS: Tracking information updated
    OMS->>NS: Notify tracking update
    NS-->>C: Shipped notification with tracking

    SC->>SC: Package delivered
    SC-->>OMS: Delivery confirmation
    OMS->>IS: Confirm delivery (decrement inventory)
    IS-->>OMS: Inventory updated
    OMS->>NS: Send order completion
    NS-->>C: Order completed notification
```

## Interface Implementations

### Internal Domain Services
- ProductCatalogService: Product discovery and category navigation
- OrderManagementService: Order lifecycle management
- InventoryService: Real-time inventory tracking and reservations
- BOPISManagementService: Pickup slot management and store coordination
- PaymentProcessingService: Payment authorization and capture

### External Integrations
- Store Management System: Store inventory synchronization
- Payment Gateway: Payment processing
- Shipping Carriers: Non-BOPIS fulfillment tracking
- Customer Notification Service: Order status updates

## TMF Alignment

**Covered APIs**:
- TMF620 (Product Catalog Management): Product catalog operations
- TMF622 (Product Ordering): Order lifecycle management
- TMF645 (Party Role Management): Customer profile management

**Uncovered APIs**:
- TMF637 (Service Ordering): Not applicable to pure product ordering
- TMF638 (Service Catalog): Service-specific catalog features

**SID Mappings**:
- Product → ProductSpecification
- Order → ProductOrder
- OrderItem → ProductOrderItem
- StockLevel → Resource / ProductOffering
- PickupSlot → ProductOffering (time-based fulfillment)

## Compliance

- PCI DSS: Payment processing compliance through certified payment gateway
- GDPR: Customer data privacy and consent management
- Accessibility: WCAG 2.1 AA compliance for customer interfaces
- Regional regulations: Location-specific fulfillment and tax compliance

## SA Conformance Report

- **NFR budget fit**: Direct domain initialization (NFRs defined within)
- **Interface conformance**: Domain-internal interfaces defined
- **Pattern conformance**: Domain-driven design patterns applied
- **Issues**: None identified

## Decisions

| ID | Decision | SA Deviation? | Review Required? |
|---|---|---|---|
| DA-001 | BOPIS implementation requires real-time store inventory integration | No | No |
| DA-002 | Payment processing delegated to certified third-party gateway | No | No |
| DA-003 | Separate aggregate for BOPIS to handle pickup slot complexity | No | Yes |

## Open Questions

- Integration points with store management systems specification
- Detailed pickup slot capacity management rules
- Multi-store inventory allocation strategy for split BOPIS orders
- Customer notification preferences and channel routing
- Returns and exchanges process for BOPIS orders