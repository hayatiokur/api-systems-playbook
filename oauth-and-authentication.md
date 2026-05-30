# Auth Systems and Token Lifecycle

## Authentication vs Authorization

Authentication --> name on the drivers license, who are you?

Authorization --> what sort of vehicle user can drive, what are you allowed to do?

Authentication happens first, authorization comes after.

## API Keys (classic ones)

Static tokens, usually has no strong connection with the user itself, more often tied to account. Usually easy to implement & use, usually have no expiration, have limited scopes depending on implementation.

They are good for simple APIs or internal services - but they are less secure overall. 

## JWT

Stands for JSON Web Token. JWT is token format, not auth protocol like Oauth. Usually used as bearer token. JWT can include claims (info) like user info, role, scope and expiration timestamp. 

Big advantage is that auth validation can happen locally, therefore they are fast and more scalable. Which can also be counted as weakness - because of the same reason immediate revocation is harder. Token usually stays valid until expiration unless additional revocation mechanisms exist. JWT often appears together with OAuth systems.

## OAuth2

OAuth2 is not token but protocol / authorization framework. It's main purpose is delegated authorization. Instead of giving credentials directly to app, user grants limited access. Google Login is common example. OAuth2 can use different token types like JWT or opaque tokens. 

## Token Lifecycle

Typical modern auth setup includes:

* Access token
* Refresh token

Access token: short lived, usually expires in minutes. 

Refresh token: longer lived - used to obtain new access token

## JWT vs API Keys

|            | API Keys             | JWT                       |
| ---------- | -------------------- | ------------------------- |
| Identity   | often app/project/entire account    | usually user/session      |
| Expiration | usually none       | usually included          |
| Claims (info carried in the token)     | limited              | rich claims               |
| Validation | server lookup common | local validation possible |
| Complexity | simple               | more complex              |
