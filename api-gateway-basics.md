# How an API Gateway Works

## Purpose
API gateways are useful when there are multiple backend services that need to work together. Instead of every service handling things like authentication, rate limiting, monitoring and routing separately, the gateway centralizes these concerns in one place.

Another big benefit is simplicity for clients. Clients do not need to know where services live or how backend infrastructure changes over time. They communicate with a single entry point while the gateway handles the complexity behind the scenes.

Here are some awesome sources to watch:

- [API Gateways Explained](https://www.youtube.com/watch?v=6ULyxuHKxg8&t=12s)
  
## Core Components

### Routing
Routing is needed because all requests come to one point first. The gateway inspects the request and decides where it should go based on predefined rules such as URL path, host or request type.

This reduces complexity for the client because the client always calls the same endpoint while backend services can evolve independently.

### Authentication and Authorization
One of the first things the API gateway does is check whether the request is authenticated and authorized. Common methods include PAT, JWT, OAuth, classic API keys. 

Authentication answers:
- Who are you?

Authorization answers:
- Are you allowed to do this?

This approach keeps authentication centralized and blocks unauthorized traffic before it reaches backend services.

### Rate Limiting
Rate limiting protects the API and backend systems from overload and abuse.

It helps:
- keep the API available
- prevent abuse and DDoS attacks  
- distribute traffic fairly
- control infrastructure and API costs   

Without rate limiting, even a healthy backend can become overloaded or unnecessarily expensive to operate.

### Plugins
Plugins are practical because they are reusable and standardized.

Instead of implementing the same functionality inside every backend service, the gateway can add these capabilities through plugins.

Common plugin examples:
- authentication  
- rate limiting  
- logging  
- monitoring  
- request transformation  

This keeps backend services simpler and reduces duplicated logic.

## Request Flow

Typical flow:

Client → Gateway → TLS handling → Authentication → Rate Limiting → Logging / Monitoring → Routing → Service → Response

The gateway performs validation and traffic management first, then forwards valid requests to the appropriate backend service.

## Benefits

Main benefits of API gateways:

- centralized security  
- simplified backend services  
- reduced duplicated logic  
- easier traffic control  
- easier monitoring and observability  
- stable interface for clients even when backend changes  

## Tradeoffs and Risks

API gateways are useful but not free.

Tradeoffs include:

- additional latency  
- operational complexity (all APIs should integrate to the GW first)  
- potential bottleneck if poorly designed  

Since all traffic passes through the gateway, failures can have large impact. This is why gateways are usually deployed with redundancy and failover mechanisms.

## Kong Example

Kong is an open source API gateway built around a plugin based architecture.

In Kong, you typically define:

- Services  
- Routes  
- Plugins  

Routes decide where requests go, while plugins provide reusable functionality such as authentication, logging and rate limiting.

This makes Kong flexible and allows teams to add gateway capabilities without changing backend services.
