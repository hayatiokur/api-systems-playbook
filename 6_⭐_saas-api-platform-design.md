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
 Data Import API
        │
        ▼
      Kafka
        │
        ▼
Transformation / Enrichment
        │
        ▼
  Product Catalog
        │
        ▼
  Export Service
        │
        ▼
      Kafka
        │
 ┌──────┼─────────┬─────────┬─────────┐
 ▼      ▼         ▼         ▼         ▼
Billing Analytics CRM Notifications Marketplace-connectors
                                        ▼
                                        │
                                 ┌──────┼─────────┬─────────┐
                                 ▼      ▼         ▼         ▼
                               Amazon eBay     Zalando  Shopify
```

```text
[MIRO DIAGRAM PLACEHOLDER]

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
        ▼
   Order Service
        │
        ▼
      Database
```

The platform acts as middleware between brands and marketplaces.

Brands send product, inventory, price and image data to the platform. The platform transforms and enriches this data before distributing it to marketplaces.

On the other side, marketplaces send orders, returns and shipment updates back to the platform.

I chose an event driven architecture because marketplace integrations are usually slow, unreliable and high volume. Kafka helps decouple the different parts of the system and makes scaling much easier.

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
Data Import API
```

Customers authenticate using OAuth2 and receive JWT access tokens.

JWT is a good fit here because authentication can happen directly at the gateway. No need to query another service for every request.

For simpler integrations, API keys can also be supported.

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
Data Import API
```

Rate limiting protects the platform from abuse and also supports monetization.

Example plans:

* Free: 100 req/min
* Pro: 1000 req/min
* Enterprise: custom

I would use sliding window rate limiting because it creates smoother traffic patterns and avoids spikes around window boundaries.

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

Logs, metrics and traces help engineers understand what is happening inside the platform.

The most important metrics would be:

* Latency
* Error Rate
* Throughput
* Success Rate

Alerts should be configured for things like latency spikes, increased error rates and unusual traffic patterns.

---

## Async Processing

```text
[MIRO DIAGRAM PLACEHOLDER]

Product Updated
        │
        ▼
 Data Import API
        │
        ▼
       Kafka
        │
        ▼
Transformation Service
        │
        ▼
 Product Catalog
```

Almost everything in the platform is event driven.

When product, inventory or pricing data arrives, an event is published to Kafka. Transformation and enrichment services consume these events and build a clean internal product catalog.

This allows ingestion and processing to scale independently.

---

## Export Processing

```text
[MIRO DIAGRAM PLACEHOLDER]

 Product Catalog
        │
        ▼
  Export Service
        │
        ▼
      Kafka
        │
 ┌──────┼─────────┬─────────┬─────────┐
 ▼      ▼         ▼         ▼         ▼
Amazon eBay     Zalando  Shopify Analytics
```

I intentionally use Kafka again before marketplace connectors.

There are several reasons for this.

First, exporting is usually slow. Different marketplaces have different APIs, rate limits and reliability. Kafka allows connectors to process data at their own speed.

Second, retries become much easier. If Amazon is temporarily unavailable, events stay in Kafka and can be retried later.

Third, a single event can be consumed by many systems. The same export event can be used by Amazon, eBay, Shopify, analytics or audit services without creating direct dependencies.

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

Different customers have different technical capabilities, so I would support multiple ways of receiving order data.

Options include:

* API Pull
* Webhook Push
* CSV/XML Export

This allows both modern and legacy systems to integrate with the platform.

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

Multiple API Gateway instances run behind a load balancer.

Kafka data is replicated across multiple brokers, so a single broker failure should not bring the platform down.

Consumer groups allow processing capacity to grow as traffic grows.

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
* * More operational complexity

### Rate Limiting

* * Protects infrastructure and supports monetization
* * Can hurt user experience if limits are too aggressive

### Event Driven Architecture

* * Highly scalable and flexible
* * Eventual consistency between systems

---

## Conclusion

I think this architecture is a good fit for a marketplace integration platform.

Brands integrate once and can communicate with many marketplaces through a single platform.

The combination of API Gateway, OAuth2, JWT, rate limiting, observability and Kafka provides a scalable and resilient foundation while still allowing the platform to evolve over time.

