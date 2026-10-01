# Deployment Guide: FastAPI on DeployHub

This guide details configuring and launching `deployhub_fastapi` on DeployHub.

## ⚙️ Configuration Manifest

```json
{
  "name": "deployhub_fastapi",
  "framework": "FastAPI",
  "runtime": "python",
  "port": 8000,
  "buildCommand": "pip install -r requirements.txt",
  "startCommand": "uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2",
  "healthCheck": {
    "path": "/api/health",
    "expectedStatus": 200,
    "timeoutSeconds": 10
  }
}
```

## 🔐 Environment Variables

| Variable | Required | Default | Description |
| :--- | :-: | :--- | :--- |
| `PORT` | No | `8000` | HTTP listening port |
| `APP_ENV` | No | `production` | Environment mode |
| `LOG_LEVEL` | No | `info` | Logging verbosity |
