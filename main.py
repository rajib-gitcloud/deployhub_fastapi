import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import health, items

app = FastAPI(
    title="DeployHub FastAPI Backend",
    description="High-performance, asynchronous REST API with automatic OpenAPI documentation.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(health.router, tags=["Health"])
app.include_router(items.router, prefix="/api", tags=["Items"])

@app.get("/", tags=["Root"])
async def root():
    return {
        "status": "healthy",
        "service": "deployhub_fastapi",
        "framework": "FastAPI",
        "docs": "/docs",
        "redoc": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
