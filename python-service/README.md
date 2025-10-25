# Python FastAPI Service

A simple FastAPI-based Python service template.

## Features

- FastAPI framework for building APIs
- Automatic API documentation at `/docs`
- Health check endpoint at `/health`
- Docker support for containerization
- Uvicorn ASGI server for production

## Getting Started

### Prerequisites

- Python 3.11+
- pip

### Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python main.py
```

or

```bash
uvicorn main:app --reload
```

The service will be available at `http://localhost:8000`

### API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Docker

### Build the Docker image:

```bash
docker build -t python-service .
```

### Run the container:

```bash
docker run -p 8000:8000 python-service
```

## Endpoints

- `GET /` - Returns a hello world message
- `GET /health` - Health check endpoint

## Development

This is a basic template that you can extend with:
- Database connections
- Authentication
- Additional endpoints
- Middleware
- Testing setup

## License

MIT

