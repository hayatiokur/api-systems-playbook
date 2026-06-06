## ⭐ Featured Work ⭐

### Designing an API Platform for a SaaS Product

This is a small system design case study that combines API gateways, authentication, rate limiting, observability and Kafka into a complete platform design.

The example platform acts as middleware between brands and marketplaces. Instead of integrating with - lets say - Amazon, eBay and other marketplaces directly, brands integrate once with the platform, which handles integrations, scaling and reliability. Product, inventory, pricing, image and order data flow through the platform. 

I assume monetization is based on API usage, marketplace integrations and transaction volume.

---

## High Level Architecture

```text
[MIRO DIAGRAM PLACEHOLDER]

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
 ┌──────┼──────┬─────────┐
 ▼      ▼      ▼         ▼
Billing Analytics CRM Notifications
```

The API Gateway acts as the entry point for all traffic. Backend services handle business logic while Kafka enables asynchronous processing for downstream systems.

This architecture keeps the platform modular. New services can subscribe to Kafka events without requiring changes to existing services. It also keeps APIs responsive because non critical work can be processed asynchronously.

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

Customers authenticate using OAuth2 and receive JWT access tokens. The gateway validates the token before routing requests.

JWT allows authentication to happen locally at the gateway without calling a central authentication service for every request. This reduces latency and scales well as traffic grows.

For server to server integrations, API keys may also be supported.

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

Rate limiting protects the platform from abuse while ensuring fair usage across customers.

Example limits:

* Free: 100 req/min
* Pro: 1000 req/min
* Enterprise: custom

The platform uses sliding window rate limiting with per account limits and global safeguards.

Burst traffic is allowed within reasonable limits to avoid hurting legitimate usage patterns.

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

Logs, metrics and traces provide visibility into platform health and behavior.

Key metrics:

* Latency
* Error Rate
* Throughput
* Success Rate

Typical alerts include spikes in 5xx errors, unusual latency increases and traffic anomalies.

Observability is critical because it allows engineers to detect and troubleshoot issues before customers notice them.

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
 ┌──────┼──────┬─────────┐
 ▼      ▼      ▼         ▼
Billing Analytics CRM Notifications
```

Not every action needs to happen during the API request.

When product, inventory or order data changes, events are published to Kafka. Downstream services consume these events independently.

This reduces coupling between services and keeps API response times low even when multiple systems need to react to the same event.

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
               Broker 1 Broker 2 Broker 3
```

Multiple gateway instances run behind a load balancer so traffic can be distributed across the platform.

Kafka brokers replicate data across the cluster. If a broker fails, another broker can take over and continue serving traffic.

Consumer groups allow event processing to scale horizontally as usage grows.

This architecture removes major single points of failure and provides a foundation for high availability.

---

## Tradeoffs

Every architectural decision introduces tradeoffs.

API Gateway:

* * Centralized routing, auth and monitoring
* * Additional infrastructure and latency

JWT:

* * Scalable and stateless
* * Token revocation is harder

Kafka:

* * Scalability, resilience and loose coupling
* * Operational complexity

Rate Limiting:

* * Infrastructure protection and monetization
* * Poorly configured limits can hurt user experience

The overall tradeoff is accepting additional system complexity in exchange for scalability, resilience and operational flexibility.

---

## Conclusion

This architecture provides a scalable platform for connecting brands and marketplaces through a single integration layer.

The combination of API Gateway, OAuth2, JWT, rate limiting, observability and Kafka creates a platform that can grow with customer demand while remaining reliable and manageable.

The biggest challenge is operational complexity, but for a platform handling large volumes of product, inventory and order data, the benefits outweigh the costs.

