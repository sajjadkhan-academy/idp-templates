# FastAPI Python Service Template

This template provides a basic FastAPI application that can be used as a starting point for creating microservices.

## Files Included

1. **main.py** - FastAPI application with hello world endpoint
2. **requirements.txt** - Python dependencies (FastAPI, Uvicorn)
3. **Dockerfile** - Docker configuration for containerization
4. **README.md** - Documentation for the service
5. **.gitignore** - Git ignore file for Python projects
6. **.dockerignore** - Docker ignore file

## Features

- FastAPI framework for high performance
- Automatic API documentation at `/docs` and `/redoc`
- Health check endpoint at `/health`
- Docker support for easy deployment
- Production-ready configuration

## Usage from IDP Dashboard

When a user creates a Python service from the IDP dashboard:

1. The user fills out the form with:
   - Component Name (e.g., "User Authentication Service")
   - Description
   - Owner
   - GitHub Repository Name (auto-generated from component name)

2. The backend will:
   - Create a new GitHub repository in the configured organization
   - Copy all template files to the new repository
   - Create a component entry in the IDP catalog

3. The user can then:
   - Clone the repository locally
   - Customize the service
   - Deploy using Docker

## Customization

After creating a service from this template, developers can:
- Add new endpoints
- Connect to databases
- Add authentication
- Implement business logic
- Configure CI/CD

## API Endpoints

- `GET /` - Returns hello world message
- `GET /health` - Health check endpoint
- `GET /docs` - Swagger UI documentation
- `GET /redoc` - ReDoc documentation

## Development

To run locally:

```bash
pip install -r requirements.txt
python main.py
```

Or using uvicorn:

```bash
uvicorn main:app --reload
```

## Docker

Build and run:

```bash
docker build -t python-service .
docker run -p 8000:8000 python-service
```

