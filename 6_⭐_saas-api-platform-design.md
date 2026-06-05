## ⭐ Featured Work ⭐

### Designing an API Platform for a SaaS Product

This is a small case study like document that combines API gateways, authentication, rate limiting, observability and Kafka into a complete platform design.

I assume the main platform is middleware that sit between brands (like adidas) and marketplaces (like amazon). Brands/retailers interact with marketplaces through this platform, they send product, order, price, image data. They use this platform because then they dont need to integrate to multiple marketplaces and this platform does error handling and handles scalibility much better. 

I assume monetization is commision (from orders) and usage (rps) based - there is a free tier and if you want to push more products or integrate to more market places, you pay more.  

---

## High Level Architecture

Add your diagram here.

Example:

Client
↓
API Gateway
↓
Backend APIs
↓
Kafka
↓
Billing / Analytics / Notifications / CRM

Explain why you chose this architecture.

---

## API Gateway

Think:
- Routing
- Single entry point
- Authentication
- Rate limiting
- Monitoring

Question:
Why not expose backend services directly?

---

## Authentication

Think:
- OAuth2
- JWT
- Refresh tokens
- API keys

Question:
How do clients authenticate?

---

## Rate Limiting

Design a policy.

Example:

Free:
- 100 req/min

Pro:
- 1000 req/min

Enterprise:
- custom

Think:
- Sliding window
- Per account limits
- Global safeguards
- Burst handling

---

## Observability

Think:
- Logs
- Metrics
- Traces

Monitor:
- Latency
- Error rate
- Throughput
- Success rate

Example alerts:
- 5xx spike
- Latency > 2 sec

---

## Async Processing

Think:
- What should happen asynchronously?

Examples:
- Billing
- Analytics
- Notifications
- CRM updates

Question:
Why use Kafka instead of direct service calls?

---

## Scalability and Resilience

Think:
- Multiple gateway instances
- Load balancer
- Kafka replication
- Failover mechanisms
- Consumer groups

Question:
What happens when a service or broker dies?

---

## Tradeoffs

Gateway:
- +

- -

JWT:
- +

- -

Kafka:
- +

- -

Rate limiting:
- +

- -

Question:
What complexity are we accepting in exchange for scalability and resilience?

---

## Conclusion

Summarize:

- Why this architecture was chosen
- Main strengths
- Main risks
