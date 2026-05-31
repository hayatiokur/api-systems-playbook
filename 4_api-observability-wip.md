# API Observability

## Purpose

Main purpose of observability is reliability, understanding system behavior, easier debugging and sometimes even security monitoring.

Without observability, understanding what is happening inside your systems becomes difficult.

## Logs vs Metrics vs Traces

### Logs

These are detailed events.

You see what has been going on. Timestamps are available so you can understand chain of events and investigate incidents.

Mostly used for debugging.

Examples:

* 401 unauthorized
* 429 too many requests
* timeout
* failed login

### Metrics

Metrics are aggregated measurements.

You can use them for debugging and sometimes security monitoring, but mainly they show performance and trends.

Metrics are commonly used for dashboards and alerts.

Typical API metrics:

* latency
* request count
* CPU usage
* error rate
* traffic volume

### Traces

This is basically request journey.

Example:

Gateway → Auth → Search Service → DB → Response

You can see where traffic travels and where latency or failures happen.

Very useful in distributed systems and microservice environments.

## Error Classification

Errors are classified to understand incidents, ownership and usage patterns.

Common categories:

4xx:

* client side issues
* bad request
* auth problems

5xx:

* server side problems
* dependency failures
* platform issues

2xx:

* successful requests

Common examples:

401 / 403:

* auth and permission problems

429:

* too many requests
* rate limiting triggered

## Core Metrics

### Latency

Basically response time or "lag".

### Error Rate

Failed requests / total requests.

### Throughput

Request volume over time.

### Success Rate

Successful requests / total requests.
