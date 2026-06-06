## ⭐ Featured Work ⭐

### Designing an API Platform for a SaaS Product

This is a small system design case study that combines API gateways, authentication, rate limiting, observability and Kafka into a complete platform design.

The example platform acts as middleware between brands and marketplaces. Instead of integrating with - lets say - Amazon, eBay and other marketplaces directly, brands integrate once with the platform, which handles integrations, scaling and reliability. Product, inventory, pricing, image and order data flow through the platform. 

I assume monetization is based on API usage, marketplace integrations and transaction volume.

---

## High Level Architecture

```text
[MIRO DIAGRAM PLACEHOLDER]

                    OUTBOUND FLOW

Brand / Retailer
        │
        ▼
   API Gateway
        │
        ▼
   Backend APIs
        │
        ▼
      Kafka
        │

        │
 ┌──────┼─────────┬─────────┬─────────┐
 ▼      ▼         ▼         ▼         ▼         
Billing Analytics CRM Notifications Marketplace-connectors
                                        ▼
                                        │
                                 ┌──────┼─────────┬─────────┐
                                 ▼      ▼         ▼         ▼
                               Amazon eBay     Zalando  Shopify



                     INBOUND FLOW

Amazon eBay     Zalando  Shopify
 ▼      ▼         ▼         ▼
 └──────┼─────────┴─────────┘
        │
        ▼
Marketplace Connectors
        │
        ▼
      Kafka
        │
 ┌──────┼─────────┬─────────┬─────────┐
 ▼      ▼         ▼         ▼         ▼
Billing Analytics CRM Notifications Order Service
                                        │
                                        ▼
                                     Database
```

The platform acts as middleware between brands and marketplaces.

Outbound events such as product updates, inventory updates and price changes are sent to marketplaces.

Inbound events such as new orders, shipment updates and returns are collected from marketplaces and stored in the platform.

---

## Authentication

```text
[MIRO DIAGRAM PLACEHOLDER]

Client
  │
  ▼
OAuth2 Login
  │
  ▼
Access Token (JWT)
  │
  ▼
API Gateway
  │
  ▼
Backend Service
```

Customers authenticate using OAuth2 and receive JWT access tokens.

JWT validation happens at the gateway, allowing requests to be authenticated without querying a central session store.

API keys may also be supported for server to server integrations.

---

## Rate Limiting

```text
[MIRO DIAGRAM PLACEHOLDER]

Client
  │
  ▼
API Gateway
  │
  ├─ Authentication
  ├─ Rate Limit Check
  └─ Routing
  │
  ▼
Backend Service
```

Rate limiting protects the platform and supports usage based monetization.

Example plans:

* Free: 100 req/min
* Pro: 1000 req/min
* Enterprise: custom

The platform uses sliding window rate limiting with per account limits and global safeguards.

---

## Observability

```text
[MIRO DIAGRAM PLACEHOLDER]

Request
  │
  ▼
Gateway
  │
  ├─ Logs
  ├─ Metrics
  └─ Traces
  │
  ▼
Monitoring Platform
```

The platform collects logs, metrics and traces to understand system behavior and troubleshoot incidents.

Key metrics:

* Latency
* Error Rate
* Throughput
* Success Rate

Alerts are configured for latency spikes, error spikes and unusual traffic patterns.

---

## Async Processing

```text
[MIRO DIAGRAM PLACEHOLDER]

Product Updated
        │
        ▼
    API Service
        │
        ▼
       Kafka
        │
 ┌──────┼─────────┬─────────┬─────────┬─────────┐
 ▼      ▼         ▼         ▼         ▼         ▼
Billing Analytics CRM Notifications Marketplace Connectors
```

The platform uses Kafka as its event backbone.

Business events such as ProductUpdated, InventoryChanged and OrderCreated are published to Kafka and processed independently by downstream services.

This reduces coupling and allows services to scale independently.

---

## Order Delivery Options

```text
[MIRO DIAGRAM PLACEHOLDER]

                   New Order

Marketplace
      │
      ▼
Connector
      │
      ▼
 Kafka
      │
      ▼
Order Service
      │
      ▼
 Database

      ├────────► API Pull
      │
      ├────────► Webhook Push
      │
      └────────► CSV/XML Export
```

Customers can receive order data through multiple mechanisms depending on their technical maturity and integration capabilities.

Supported options:

* Pull via API
* Push via Webhooks
* Scheduled CSV/XML exports

---

## Scalability and Resilience

```text
[MIRO DIAGRAM PLACEHOLDER]

                Load Balancer
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
    Gateway 1      Gateway 2      Gateway 3
                       │
                       ▼
                  Kafka Cluster

        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Broker 1       Broker 2       Broker 3
```

Multiple gateway instances run behind a load balancer.

Kafka brokers replicate data across the cluster and consumer groups allow horizontal scaling.

If a gateway instance, service or broker fails, the platform continues operating with minimal disruption.

---

## Tradeoffs

### API Gateway

* * Centralized authentication, routing and monitoring
* * Additional infrastructure and latency

### JWT

* * Stateless and scalable
* * Token revocation is harder

### Kafka

* * Scalability, resilience and loose coupling
* * Higher operational complexity

### Rate Limiting

* * Infrastructure protection and monetization
* * Aggressive limits may hurt user experience

### Event Driven Architecture

* * Highly scalable and resilient
* * Eventual consistency between systems

---

## Conclusion

This architecture provides a scalable marketplace integration platform where brands integrate once and communicate with many marketplaces.

The combination of API Gateway, OAuth2, JWT, rate limiting, observability and Kafka creates a resilient platform that can process large volumes of product, inventory and order data while remaining flexible and extensible.

