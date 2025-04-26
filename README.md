# Webhook Delivery Service

[![Deployed on Render](https://img.shields.io/badge/Deployed-Render.com-blue?logo=render&logoColor=white)](https://webhook-delivery-service-9.onrender.com)

A robust backend system for reliable webhook ingestion, queuing, delivery retries, caching, and status tracking.  
Built with **FastAPI**, **Celery**, **Redis**, **PostgreSQL**, and **Docker**.

---

## 📚 Features

- Subscription Management (CRUD)
- Webhook Ingestion with fast 202 Accepted
- Asynchronous Delivery with Retry and Exponential Backoff
- Delivery Status Logging and Tracking
- Signature Verification (HMAC-SHA256)
- Event Type Filtering (Optional)
- Caching Subscription Details (Redis)
- Periodic Cleanup of Delivery Logs (older than 72h)
- Fully Containerized (Docker, docker-compose)
- Swagger UI available at `/docs`

---

## 🛠 Tech Stack

- Python 3.11
- FastAPI (Web Framework)
- Celery (Background Workers)
- Redis (Queue + Cache)
- PostgreSQL (Database)
- Docker and Docker Compose

---

## 🚀 Local Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/ANKITKUMARSINGH2004/webhook-delivery-service.git
cd webhook-delivery-service
```

2. **Set Environment Variables**

```bash
cp .env.example .env
```

3. **Run with Docker Compose**

```bash
docker-compose up --build
```

4. **Access API Documentation**

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📈 Architecture Overview

```plaintext
[Client] → [FastAPI API Server] → [Redis Queue] → [Celery Workers]
                                    ↓
                               [PostgreSQL Logs]
```

---

## 🧪 Sample cURL Commands

### Create a Subscription

```bash
curl -X POST "http://localhost:8000/subscriptions/" -H "Content-Type: application/json" -d '{"target_url":"http://example.com/webhook","secret":"your_secret_key","event_type":"order.created"}'
```

### Ingest Webhook

```bash
curl -X POST "http://localhost:8000/ingest/1" -H "Content-Type: application/json" -d '{"body":"payload_content","signature":"computed_signature"}'
```

### Get Delivery Status

```bash
curl "http://localhost:8000/status/{task_id}"
```

### List Recent Deliveries for a Subscription

```bash
curl "http://localhost:8000/subscriptions/1/deliveries"
```

---

## 🎨 Why This Design?

- **FastAPI**: Lightweight, fast, and comes with built-in automatic Swagger documentation.
- **Celery**: Best for managing background asynchronous tasks and retrying failed webhook deliveries.
- **Redis**: Perfect as both a broker (queue) and cache layer — high-speed and lightweight.
- **PostgreSQL**: Reliable SQL database, optimized for transactional logging and indexing.
- **Docker + docker-compose**: Ensures smooth, isolated development and production deployments.
- **Retry Mechanism**: Exponential backoff ensures not overloading target systems while maintaining delivery reliability.
- **Signature Verification**: Adds security to ensure payload authenticity if a secret is provided.
- **Event Filtering**: Supports efficient event-driven architecture if needed by the client systems.

---

## 🔮 Future Improvements

- Implement rate limiting per subscription to prevent webhook flooding.
- Add dynamic webhook delivery headers based on subscription preferences.
- Implement real-time WebSocket monitoring for delivery status.
- Add detailed metrics (Prometheus + Grafana) for operational visibility.
- Support batch ingestion of multiple webhooks for better throughput.

---

## ✅ Testing

- Unit tests created for subscription management, webhook ingestion, and retry mechanisms.
- To run tests (example command):

```bash
docker-compose run api pytest
```

---

## ⚡ Deployment (Optional)

You can deploy easily on **Render.com** (Free tier):

- Choose Docker deployment.
- Set environment variables:
  - `DATABASE_URL`
  - `REDIS_URL`
- Connect your GitHub repo directly.

---

## 💵 Estimated Cost (Free Tier)

| Service      | Cost   |
|:-------------|:-------|
| PostgreSQL   | Free   |
| Redis        | Free   |
| Render App   | Free   |
| **Total**    | **$0/month** |

(Enough for ~5,000 webhook ingestions/day.)

---

## 📋 Assumptions

- Webhook targets are standard POST endpoints.
- Secret verification is optional (HMAC-SHA256).
- Event types can be optionally specified.
- Logs older than 72 hours are auto-deleted.

---

## 📢 Credits

- FastAPI documentation
- Celery documentation
- Redis documentation
- SQLAlchemy documentation

