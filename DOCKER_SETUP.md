# Incident Management System - Docker Deployment Guide

## Quick Start

### Prerequisites
- Docker 20.10+
- Docker Compose 2.0+

### Build and Run

```bash
# Build all services
docker-compose build

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## Service Architecture

### Services
1. **Backend** (FastAPI)
   - URL: http://localhost:8000
   - Health: http://localhost:8000/health
   - API: http://localhost:8000/api/
   - Docs: http://localhost:8000/docs

2. **Frontend** (React with Nginx)
   - URL: http://localhost:3000 (via nginx reverse proxy)
   - Direct: http://localhost:3000 (when nginx routing)

3. **Nginx Reverse Proxy**
   - URL: http://localhost:80
   - Routes `/api/` → backend:8000
   - Routes `/` → frontend:80

## Configuration

### Environment Variables
Create a `.env` file from `.env.example`:
```bash
cp .env.example .env
```

### Nginx Configuration
- **Main Reverse Proxy**: `./nginx/nginx.conf`
- **Frontend Server**: `./frontend/nginx-frontend.conf` (built into frontend container)

## Networking
All services communicate via `ims-network` bridge network (Docker Compose internal DNS).

Service names as hostnames:
- `ims_backend` → Backend container
- `ims_frontend` → Frontend container
- `ims_nginx` → Nginx reverse proxy

## Health Checks
Each service includes health checks:
- Backend: HTTP GET /health
- Frontend: HTTP GET /
- Nginx: HTTP GET /health

## Logs and Debugging

```bash
# View all logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f nginx

# Execute command in running container
docker-compose exec backend bash
docker-compose exec frontend sh
```

## Troubleshooting

### Backend not responding
```bash
docker-compose logs backend
docker-compose exec backend curl http://localhost:8000/health
```

### Frontend not loading
```bash
docker-compose logs frontend
docker-compose exec frontend curl http://localhost/
```

### Nginx routing issues
```bash
docker-compose logs nginx
docker-compose exec nginx curl http://localhost:80/health
```

### Rebuild specific service
```bash
docker-compose build --no-cache backend
docker-compose up -d backend
```

## Production Deployment

For production, consider:
1. Using environment-specific `.env` files
2. Enabling HTTPS/SSL in nginx
3. Adding database services (PostgreSQL, MongoDB, Redis)
4. Implementing proper logging and monitoring
5. Using health checks for orchestration
6. Resource limits and cpu/memory constraints

## File Structure

```
Incident-Management-System/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── main.py
├── frontend/
│   ├── Dockerfile
│   ├── nginx-frontend.conf
│   └── package.json
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
├── .dockerignore
└── .env.example
```
