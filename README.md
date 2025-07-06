# Task Manager API

## Description

A FastAPI-based Task Manager application with PostgreSQL database integration. This project provides a simple API for managing tasks, including creating and listing tasks. It also includes database connection checks and follows modern Python web development practices.

## Features

- RESTful API endpoints for task management
- PostgreSQL database integration
- Database migration support using Alembic
- Containerized with Docker for easy deployment
- Environment variable configuration

## Usage

1. Clone the repository
2. Run the application using Docker Compose:

```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`. Available endpoints:

- `GET /` - Welcome message
- `GET /users/db` - Check database connection
- `POST /tasks` - Create a new task
- `GET /tasks` - List all tasks

## Technologies

- Python 3.10
- FastAPI
- SQLAlchemy (ORM)
- PostgreSQL
- Alembic (database migrations)
- Docker
- Pydantic (data validation)
