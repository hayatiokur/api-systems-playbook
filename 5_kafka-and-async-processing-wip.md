# Async Systems and Apache Kafka

## Purpose

Kafka provides an event driven architecture, it is great for decoupling different crucial services, it is resilient and scalable. 

## Core Concepts

### Producers

This could be anything that "produce" and write messages such as an API, order data, new users, updated product data etc.  

---

### Topics

Think:

* Logical channel for messages
* How are messages grouped?

Examples:

* user-events
* billing-events
* analytics-events

---

### Partitions

Think:

* Why split a topic?
* Parallel processing
* Higher throughput
* Ordering only guaranteed within partition

---

### Brokers and Clusters

Think:

* What is a broker?
* Why multiple brokers?
* What is a Kafka cluster?

Question:
What happens if one broker dies?

---

### Consumers and Consumer Groups

Think:

* Who processes events?
* Why consumer groups?

Keywords:

* scaling
* load distribution
* parallel processing

---

## Why Kafka is Resilient

Think:

* replication
* leader and followers
* failover
* no single point of failure

Question:
Why do large companies trust Kafka for critical workloads?

---

## Semrush Example

Event:
User subscribed

Producer:
Subscription Service

Topic:
user-subscriptions

Consumers:

* Billing
* Analytics
* CRM
* Email Service

Question:
Why is this better than calling all services directly?

---

## Tradeoffs

Think:

Benefits:

* scalability
* resilience
* loose coupling

Challenges:

* more complexity
* eventual consistency
* debugging becomes harder

<img width="1536" height="1024" alt="Kafka, 2026, 06_39_59 PM" src="https://github.com/user-attachments/assets/a5d8cef2-d56c-40d8-951f-035968f3dd47" />
