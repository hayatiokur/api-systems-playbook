## ⭐ Featured Work ⭐

### Designing an API Platform for a SaaS Product

This is a small system design case study that combines API gateways, authentication, rate limiting, observability and Kafka into a complete platform design.

The example platform acts as middleware between brands and marketplaces. Instead of integrating with - lets say - Amazon, eBay and other marketplaces directly, brands integrate once with the platform, which handles integrations, scaling and reliability. Product, inventory, pricing, image and order data flow through the platform. 

I assume monetization is based on API usage, marketplace integrations and transaction volume.

---

## High Level Architecture

### Outbound Flow

<img width="1259" height="794" alt="image" src="https://github.com/user-attachments/assets/c64a5200-a6a0-4644-bca0-979ea10b11c6" />

### Inbound Flow

<img width="1673" height="597" alt="image" src="https://github.com/user-attachments/assets/1fd36350-8cda-4a91-8bc5-9b8391553c3f" />

The platform acts as middleware between brands and marketplaces.

Brands send product, inventory, pricing and image data to the platform. The platform validates, transforms and enriches this data before distributing it to different marketplaces.

Marketplaces also send data back, such as new orders, shipment updates and returns.

I chose an event driven architecture because marketplace integrations are usually slow, unreliable and high volume. Kafka helps decouple different parts of the system and makes scaling easier.

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
Data Import APIs
```

Customers authenticate using OAuth2 and receive JWT access tokens.

JWT is a good fit because authentication can happen directly at the API Gateway without calling another service for every request.

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
Data Import APIs
```

Rate limiting protects the platform from abuse and also supports monetization.

Example plans:

* Free: 100 req/min
* Pro: 1000 req/min
* Enterprise: custom

I would use sliding window rate limiting because it creates smoother traffic patterns and avoids spikes around window boundaries.

---

## Observability

Logs, metrics and traces help engineers understand what is happening inside the platform.

The most important metrics would be:

* Latency
* Error Rate
* Throughput
* Success Rate

Alerts should be configured for latency spikes, increased error rates and unusual traffic patterns.

---

## Async Processing

Almost everything in the platform is event driven.

When product, inventory or pricing data arrives, an event is published to Kafka. Transformation and enrichment services consume these events and build a clean internal product catalog.

Invalid data should not enter the catalog. Validation errors should be logged and exposed to customers so they can fix data quality issues.

---

## Export Processing

The platform uses Kafka again before marketplace connectors.

Different marketplaces process data at different speeds and sometimes become unavailable.

Kafka allows connectors to consume data independently, retry failed exports and scale separately from the rest of the platform.

A single export event can also be consumed by multiple systems without creating tight dependencies.

---

## Failed Exports (DQL)

Marketplace APIs fail sometimes.

Instead of losing data, failed exports are sent to a Dead Letter Queue (DLQ) for investigation and retry.

This improves reliability and prevents data loss.

---

## Order Delivery Options

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

* * Scalable, resilient and loosely coupled
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
