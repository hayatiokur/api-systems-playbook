# Rate Limiting and Scaling

## Purpose

Rate limiting is a must not only because as DDOS protection but also for providing abuse prevention, fairness and even cost control for the user. 

There are two type of limiting:

* Fixed Window (100 req per min)
* Sliding Window (100 req in the LAST min)

Sliding window is difficult to calculate but provides more smooth load on your server, preventing spikes. 

You can also rate limit your APIs based on user, account, IP, per service or globally depending on your need. 

## Burst Handling & Tradeoffs

You should also think of what load your API can handle and how users use it when rate limiting. Lets say you set 1 req per second rate limiting. But your user is slient for hours and wants/needs to make 60 request in one second. Such policy would hurt such a user. So when providing rate limiting policy, you should consider your infrastructure as well as the natural user behaviour.
