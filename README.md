# DeployHub FastAPI Backend

[![DeployHub Compatible](https://img.shields.io/badge/DeployHub-Ready-brightgreen.svg)](https://deployhub.dev)
[![Framework](https://img.shields.io/badge/Framework-FastAPI%200.110+-teal.svg)](https://fastapi.tiangolo.com)
[![Language](https://img.shields.io/badge/Language-Python%203.11+-blue.svg)]()
[![Swagger UI](https://img.shields.io/badge/Docs-Swagger%20OpenAPI-brightgreen.svg)]()

High-performance, asynchronous REST API starter template built with FastAPI, Pydantic v2, and Uvicorn.

---

## 🚀 Quick Reference

- **Language / Runtime**: Python 3.11+
- **Framework**: FastAPI
- **Server**: Uvicorn ASGI Server
- **Default Port**: `8000`
- **Health Check**: `GET /api/health`
- **Interactive Docs**: `http://localhost:8000/docs`

---

## 📁 Project Structure

```text
deployhub_fastapi/
├── routers/
│   ├── health.py            # Health probe and Info endpoint
│   └── items.py             # CRUD REST API endpoints with Pydantic validation
├── deployhub.json           # DeployHub deployment manifest
├── DEPLOYMENT.md            # Cloud deployment guide
├── Dockerfile               # Multi-worker async container
├── main.py                  # Application entrypoint & middleware
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🛠 Local Setup & Running

```bash
# 1. Setup virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run with live reload
uvicorn main:app --reload --port 8000
```

---

## 🐳 Docker Execution

```bash
# Build container image
docker build -t deployhub-fastapi:latest .

# Run container
docker run -d -p 8000:8000 --name fastapi_backend deployhub-fastapi:latest
```

Test endpoint: `curl http://localhost:8000/api/health`
