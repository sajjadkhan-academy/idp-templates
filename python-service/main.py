from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Python Service", version="1.0.0")


@app.get("/")
async def root():
    """Root endpoint that returns a hello world message."""
    return {"message": "Hello World!"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

