# Apache Kafka

## Purpose

Kafka provides an event driven architecture. It is great for decoupling (crucial) services, improving scalability and building resilient systems. Instead of services calling each other directly, they communicate through events.

## Core Concepts

### Producers
This could be anything that produces and writes messages such as APIs, order systems, user services or product services. Examples: product updated, new user created, order completed etc.

### Topics

Messages in the qeueu are process and stored in topics and they are usually grouped by business domain or event type.

### Partitions

Topics can be split into multiple partitions. Partitions allow Kafka to process messages in parallel and achieve much higher throughput. One important detail is that message ordering is only guaranteed within the same partition.

### Brokers and Clusters

A broker is a Kafka server that stores and serves messages. Multiple brokers form a Kafka cluster. Kafka distributes partitions across brokers and usually keeps replicas on different brokers. If one broker dies, another broker can become leader and continue serving traffic. This is one of the main reasons Kafka is considered resilient.

### Consumers and Consumer Groups

This is the opposite of producers. Consumers are systems that read messages from Kafka topics. Example: CRM, Analytics etc. Consumer groups allow multiple consumers to share the workload and process messages in parallel. This improves scalability and prevents a single consumer from becoming a bottleneck.

## Tradeoffs

As explained above, Kafka is great for scalability, throughput and resilience. However, it also adds significant complexity. Debugging becomes harder because requests are no longer moving through a simple synchronous flow. Kafka clusters also require monitoring, maintenance and engineers who understand distributed systems.

If a company runs a relatively small system, can tolerate occasional delays or data loss, and does not need large scale event processing, Kafka may be unnecessary complexity.

![Kafka Architecture](https://github.com/user-attachments/assets/a5d8cef2-d56c-40d8-951f-035968f3dd47)
