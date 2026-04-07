# Portfolio Backend Service

Django REST API backend for the portfolio at [www.initial-commit.com](https://www.initial-commit.com).

## Tech Stack

- **Django 6** with Django REST Framework
- **PostgreSQL** as database
- **Gunicorn + Uvicorn** as ASGI server
- **Docker** for containerization
- **uv** for dependency management

## Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/) (for local development)
- PostgreSQL (for production, running on the host)

## Local Development

```bash
docker compose up
```

This starts both the PostgreSQL database and the Django app using the `local` target. The app is accessible at http://localhost:8000.

Environment variables are loaded from `.env.dev`.

## Production Deployment

Production runs as a standalone Docker container connecting to a host-level PostgreSQL instance.

### 1. Configure environment

Create a `.env` file in the project root. Use [.env.dev](.env.dev) as a reference. Key variables:

| Variable | Description |
|---|---|
| `DATABASE_HOST` | PostgreSQL host (e.g. `172.17.0.1` for Docker bridge) |
| `DATABASE_NAME` | Database name |
| `DATABASE_USER` | Database user |
| `DATABASE_PASSWORD` | Database password |
| `SECRET_KEY` | Django secret key |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts |
| `CSRF_TRUSTED_ORIGINS` | Comma-separated list of trusted origins |
| `DEBUG` | Set to `False` in production |

**Important:** Do not quote values in `.env` — Docker `--env-file` passes quotes literally.

### 2. Build and run

```bash
# Build the production image
docker build --target deploy -t portfolio-backend-service .

# Start the container
docker run -d \
  --name portfolio-backend \
  --env-file .env \
  -p 8000:8000 \
  --restart unless-stopped \
  portfolio-backend-service
```

The entrypoint automatically runs migrations, collects static files, and starts Gunicorn on port 8000.

### 3. Update after changes

```bash
docker rm -f portfolio-backend
docker build --target deploy -t portfolio-backend-service .
docker run -d \
  --name portfolio-backend \
  --env-file .env \
  -p 8000:8000 \
  --restart unless-stopped \
  portfolio-backend-service
```

### 4. View logs

```bash
docker logs -f portfolio-backend
```

## Nginx

In production, an external Nginx reverse proxy (managed separately) handles TLS termination and forwards traffic to port 8000. The Nginx setup uses [JonasAlfredsson/docker-nginx-certbot](https://github.com/JonasAlfredsson/docker-nginx-certbot) for automatic Let's Encrypt certificates.

Connect the backend container to the Nginx network so Nginx can reach it by container name:

```bash
docker network connect nginx_app-network portfolio-backend
```

## Project Structure

- `conf/` — Django project settings, URLs, ASGI/WSGI config
- `api/` — REST API app (models, serializers, views, URLs)
- `core/` — Core app with management commands (e.g. `wait_for_db`)

## License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.
