# Auth Systems and Token Lifecycle

## Authentication vs Authorization

Authentication --> name on the drivers license, who are you?

Authorization --> what sort of vehicle user can drive, what are you allowed to do?

Authentication happens first, authorization comes after.

## API Keys (classic ones)

Static tokens, usually has no strong connection with the user itself, more often tied to app or project identity. Usually easy to implement & use, may have no expiration, may have limited scopes depending on implementation.

Good for:

* server to server communication
* simple APIs
* internal systems

Limitations:

* weaker identity model
* sometimes broad permissions
* historically less secure if badly managed

## JWT

JSON Web Token.

JWT is token format, not auth protocol. Usually used as bearer token. JWT can include claims like:

* user id
* role
* scope
* expiration

Big advantage is that auth validation can happen locally by validating token signature, therefore scalable and fast. Which can also be counted as weakness - because of the same reason immediate revocation is harder. Token usually stays valid until expiration unless additional revocation mechanisms exist. JWT often appears together with OAuth systems.

## OAuth2

OAuth2 is not token but protocol / framework. It's main purpose is delegated authorization. Instead of giving credentials directly to app, user grants limited access. Google Login is common example. OAuth2 can use different token types:

* JWT
* opaque tokens

Usually bundled with JWT access tokens in modern systems. Important distinction: OAuth2 is framework. JWT is token format.

## Token Lifecycle

Typical modern auth setup includes:

* Access token
* Refresh token

Access token:

* short lived
* used to call APIs
* often JWT

Refresh token:

* longer lived
* used to obtain new access token
* usually stored more carefully

Typical flow:

Login
↓
Access token + Refresh token
↓
Access token used for API calls
↓
Access token expires
↓
Refresh token gets new access token
↓
No need to log in again

This setup balances:

* security
* scalability
* user experience

## JWT vs API Keys

|            | API Keys             | JWT                       |
| ---------- | -------------------- | ------------------------- |
| Identity   | often app/project    | usually user/session      |
| Expiration | sometimes none       | usually included          |
| Claims (info carried in the token)     | limited              | rich claims               |
| Validation | server lookup common | local validation possible |
| Complexity | simple               | more complex              |

Typical use cases:

API Keys:

* simple integrations
* internal APIs
* server to server

JWT:

* OAuth access tokens
* public APIs
* user authentication

## Tradeoffs

No auth system is perfect.

API keys:

* simpler
* easier
* sometimes weaker

JWT:

* scalable
* richer
* harder revocation

OAuth2:

* secure
* flexible
* more complexity

Architecture depends on:

* scale
* security
* UX requirements
* operational complexity
