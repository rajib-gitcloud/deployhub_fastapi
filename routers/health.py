import sys
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class HealthResponse(BaseModel):
    status: str
    service: str
    framework: str
    python_version: str

@router.get("/api/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        service="deployhub_fastapi",
        framework="FastAPI",
        python_version=sys.version.split()[0]
    )

@router.get("/api/info")
async def app_info():
    return {
        "app_name": "DeployHub FastAPI Backend",
        "version": "1.0.0",
        "description": "Async API starter with automatic OpenAPI docs & Pydantic validation.",
        "endpoints": [
            {"path": "/", "method": "GET", "desc": "Root health check"},
            {"path": "/api/health", "method": "GET", "desc": "Health check probe"},
            {"path": "/api/items", "method": "GET", "desc": "List sample items"},
            {"path": "/docs", "method": "GET", "desc": "Interactive Swagger UI"}
        ]
    }
