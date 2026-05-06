You are a Principal Staff Engineer and Distributed Systems Architect.

Build a production-grade Mission-Critical Incident Management System (IMS).

The system must be designed like a real enterprise platform capable of handling:
- high-throughput signal ingestion
- async event processing
- incident lifecycle workflows
- RCA enforcement
- real-time dashboarding
- resilient distributed architecture

The implementation must prioritize:
- scalability
- concurrency safety
- resiliency
- clean architecture
- maintainability
- observability
- production deployment readiness

====================================================
ASSIGNMENT REQUIREMENTS
====================================================

The platform monitors distributed infrastructure:
- APIs
- MCP Hosts
- Distributed Caches
- Async Queues
- PostgreSQL/RDBMS
- MongoDB/NoSQL

The system receives high-volume failure signals and must:
1. ingest signals asynchronously
2. debounce duplicate incidents
3. persist raw payloads
4. manage incident workflow
5. enforce mandatory RCA before closure
6. expose a real-time dashboard

====================================================
TECH STACK (MANDATORY)
====================================================

Backend:
- FastAPI
- Async SQLAlchemy
- PostgreSQL
- MongoDB
- Redis
- Pydantic v2

Frontend:
- React
- Vite
- TypeScript
- TailwindCSS

Infra:
- Docker Compose
- nginx reverse proxy

====================================================
ARCHITECTURE REQUIREMENTS
====================================================

Use the following architecture:

1. PostgreSQL
Purpose:
- source of truth
- structured incidents
- RCA records
- transactional workflow state

2. MongoDB
Purpose:
- raw signal payloads
- append-only audit log
- schemaless storage

3. Redis
Purpose:
- debounce logic
- rate limiting
- hot dashboard cache
- pub/sub
- transient state

4. nginx
Purpose:
- single entry point
- reverse proxy
- serve frontend build
- route /api to backend

====================================================
HIGH-THROUGHPUT INGESTION
====================================================

Design ingestion for burst traffic:
- up to 10,000 signals/sec

Requirements:
- async non-blocking processing
- system must not crash if DB becomes slow
- apply backpressure protection
- bounded memory usage
- proper connection pooling

Implement:
- asyncio.Queue OR background worker architecture
- ingestion buffering
- graceful degradation

====================================================
DEBOUNCING LOGIC
====================================================

If 100 signals arrive for same component within 10 seconds:
- create ONLY ONE incident/work item
- attach all signals to same work item

Implement using Redis TTL keys:
Pattern:
debounce:{component_id}

Requirements:
- atomic
- race-condition safe
- high-performance

====================================================
RATE LIMITER
====================================================

Implement Redis-based rate limiting using:
- INCR
- EXPIRE

Protect ingestion endpoint from overload.

Return:
HTTP 429 on limit exceeded.

====================================================
WORKFLOW ENGINE
====================================================

Implement incident lifecycle:

OPEN
→ INVESTIGATING
→ RESOLVED
→ CLOSED

Use proper design patterns.

Requirements:
- invalid transitions rejected
- concurrency safe updates
- transactional state changes

Implement:
- State Pattern OR transition registry

====================================================
MANDATORY RCA
====================================================

System MUST reject closing incident unless:
- RCA exists
- RCA fields complete

RCA fields:
- root cause category
- fix applied
- prevention steps
- incident start time
- incident end time

Enforce:
- backend validation
- database-level constraints where possible

====================================================
MTTR CALCULATION
====================================================

Automatically calculate:
MTTR = RCA end_time - incident first_signal_time

Persist calculated MTTR.

====================================================
ALERTING STRATEGY
====================================================

Different components produce different severity.

Examples:
- RDBMS failure → P0
- Cache failure → P2

Use Strategy Pattern:
- abstract alert strategy
- pluggable implementations

Must support easy future extension.

====================================================
CACHE DESIGN
====================================================

Maintain hot dashboard cache in Redis.

Requirements:
- avoid hitting PostgreSQL repeatedly
- 5-minute TTL
- invalidate cache on updates

====================================================
OBSERVABILITY
====================================================

Implement:
1. /health endpoint
2. throughput metrics every 5 seconds
3. structured logging
4. request timing middleware

Console metrics example:
Signals/sec: 8421

====================================================
FRONTEND REQUIREMENTS
====================================================

Build responsive dashboard with:

1. Live Feed
- active incidents
- sorted by severity

2. Incident Detail Modal/Page
- raw signals from MongoDB
- workflow state
- timestamps

3. RCA Form
Fields:
- incident start/end
- category dropdown
- fix applied
- prevention steps

4. Stats Bar
Show:
- total incidents
- open incidents
- active P1/P0
- average MTTR

====================================================
FRONTEND ENGINEERING
====================================================

Use:
- React hooks
- clean component architecture
- reusable API layer
- loading states
- optimistic updates where appropriate

Auto-refresh dashboard every 30 seconds.

====================================================
PROJECT STRUCTURE
====================================================

Create:

/backend
/frontend
/nginx
/docs

Backend structure must include:
- api/
- models/
- services/
- repositories/
- workers/
- strategies/
- state_machine/
- cache/
- middleware/
- core/
- tests/

====================================================
DOCKER REQUIREMENTS
====================================================

Provide complete Docker Compose setup.

Services:
- frontend
- backend
- postgres
- mongodb
- redis
- nginx

Requirements:
- healthchecks
- restart unless-stopped
- proper dependency ordering
- environment variables
- persistent volumes

====================================================
README REQUIREMENTS
====================================================

Generate professional README including:

1. Architecture Diagram
2. Design Decisions
3. Tech Stack Justification
4. Backpressure Handling
5. Scaling Strategy
6. Setup Instructions
7. API Documentation
8. Tradeoffs
9. Future Improvements

====================================================
TESTING REQUIREMENTS
====================================================

Add:
- unit tests
- RCA validation tests
- transition tests
- debounce tests

Use:
- pytest

====================================================
CODE QUALITY REQUIREMENTS
====================================================

Requirements:
- SOLID principles
- repository pattern
- dependency injection
- typed code
- async-first implementation
- production-level error handling
- retry decorators with exponential backoff

====================================================
OUTPUT FORMAT
====================================================

Generate the project incrementally in this order:

1. High-level architecture explanation
2. Folder structure
3. Docker Compose
4. Backend implementation
5. Database models
6. Redis logic
7. Workflow engine
8. API endpoints
9. Frontend implementation
10. nginx config
11. Tests
12. README

For every file:
- provide full code
- include path above code block

Never generate pseudo-code.
Generate runnable production-quality code only.

Explain critical architectural decisions briefly after implementation sections.

Avoid toy examples.

====================================================
BONUS FEATURES
====================================================

If possible, additionally implement:
- WebSocket live updates
- retry queue
- dead-letter queue
- OpenTelemetry hooks
- Prometheus metrics
- Swagger docs
- CI/CD workflow
- Kubernetes manifests

====================================================
IMPORTANT ENGINEERING CONSTRAINTS
====================================================

1. Avoid blocking calls inside async routes.
2. Ensure Redis operations are atomic where required.
3. Prevent race conditions in incident transitions.
4. Ensure database writes are transactional.
5. Make frontend production-ready.
6. Do not use simplistic in-memory solutions.
7. Optimize for readability and extensibility.

Think like a Staff Engineer building a real production platform.