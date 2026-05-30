# How an API Gateway Works

## Purpose
API gateways are useful when there are multiple backend services that need to work together. Instead of every service handling things like authentication, rate limiting, monitoring and routing separately, the gateway centralizes these concerns in one place.

Another big benefit is simplicity for clients. Clients do not need to know where services live (urls) or how backend infrastructure changes over time. They communicate with a single entry point while the gateway handles the complexity behind the scenes.

Here is an awesome sources to watch:

- [API Gateways Explained](https://www.youtube.com/watch?v=6ULyxuHKxg8&t=12s)
  
## Core Components

### Routing
Routing is needed because all requests come to one point first. The gateway inspects the request and decides where it should go based on predefined rules such as URL path, host or request type.

As mentioned above, this reduces complexity for the client because the client always calls the same endpoint while backend services can evolve independently.

### Authentication and Authorization
One of the first things the API gateway does is check whether the request is authenticated and authorized. Common methods include PAT, JWT, OAuth, classic API keys. 

Authentication answers:
- Who are you? (name on the drivers license)

Authorization answers:
- Are you allowed to do this? (what vehicle you can drive)

This approach keeps authentication centralized and blocks unauthorized traffic before it reaches backend services.

### Rate Limiting
Rate limiting protects the API and backend systems from overload and abuse. It provides fair usage and controls API cost for the user (and for the infrastructure)

### Plugins
Plugins are practical because they are reusable and standardized. Instead of implementing the same functionality inside every backend service, the gateway can add these capabilities through plugins. Plugins exist for authentication, rate limiting, logging and monitoring. 

## Request Flow

Typical flow:

Client → Gateway → checking if the connection is secure (TLS handling) → Authentication → Rate Limiting → Logging / Monitoring → Routing → Service → Response

The gateway performs validation and traffic management first, then forwards valid requests to the appropriate backend service.

## Benefits

Main benefits of API gateways centalized security, reduced duplicate logic, easier monitoring and observability and stable interface for clients even when backend changes and unified API behavior (very underrated). 

However there are tradeoffs such as latency and operational complexity (all APIs should integrate to the GW first). API gateways are potential bottleneck if poorly designed. Since all traffic passes through the gateway, failures can have large impact. This is why gateways are usually deployed with redundancy and failover mechanisms.
