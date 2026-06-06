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
```

```text

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

For outbound traffic, brands send product, inventory, pricing and image data to the platform. The platform then distributes this data to one or more marketplaces.

For inbound traffic, marketplaces send order, shipment and return information back to the platform. This data is stored and later made available to customers.

The platform is designed around Kafka. Almost everything becomes an event, which makes the system easier to scale and extend over time.

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

I chose JWT because the API Gateway can validate tokens directly without calling another service on every request. This keeps authentication fast and scalable.

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
Backend Service
```

Rate limiting protects the platform from abuse and also supports monetization.

Example plans:

* Free: 100 req/min
* Pro: 1000 req/min
* Enterprise: custom

I would use sliding window rate limiting because it creates smoother traffic patterns and avoids traffic spikes around window boundaries.

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

The most important metrics would probably be:

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
    API Service
        │
        ▼
       Kafka
        │
 ┌──────┼─────────┬─────────┬─────────┬─────────┐
 ▼      ▼         ▼         ▼         ▼         ▼
Billing Analytics CRM Notifications Marketplace Connectors
```

Kafka is the backbone of the platform.

When something happens, for example a product update, inventory update or new order, an event is published to Kafka.

Different systems can then react independently. Marketplace connectors, analytics, billing and notification services can all process the same event without being directly connected to each other.

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

Consumer groups allow processing capacity to grow as platform traffic grows.

---

## Tradeoffs

### API Gateway

* * Centralized routing, authentication and monitoring
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


