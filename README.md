# Webhook Delivery Service

A robust backend service for reliable webhook ingestion, queuing, delivery with retries, caching, and status tracking.  
Built with **FastAPI**, **Celery**, **Redis**, **PostgreSQL**, and **Docker**.

---

## 📚 Features

- Subscription Management (CRUD)
- Webhook Ingestion with fast acknowledgment (202 Accepted)
- Asynchronous Delivery with Exponential Backoff Retry
- Delivery Status Logging and Viewing
- Signature Verification (HMAC-SHA256)
- Event Type Filtering
- Caching Subscription Data (Redis)
- Periodic Cleanup of Delivery Logs (older than 72h)
- Fully Containerized (Docker, docker-compose)

---

## 🛠 Tech Stack

- Python 3.11
- FastAPI
- PostgreSQL (Database)
- Celery (Async Task Queue)
- Redis (Broker + Cache)
- Docker, Docker Compose

---

## 🚀 Local Setup Instructions

1. **Clone Repository**

```bash
git clone https://github.com/ANKITKUMARSINGH2004/webhook-delivery-service.git
cd webhook-delivery-service

Set Environment Variables

bash
Copy
Edit
cp .env.example .env
Run via Docker Compose

bash
Copy
Edit
docker-compose up --build
Access API Documentation

Swagger UI: http://localhost:8000/docs

🧪 Sample CURL Commands
Create Subscription
bash
Copy
Edit
curl -X POST "http://localhost:8000/subscriptions/" -H "Content-Type: application/json" -d '{"target_url":"http://example.com/webhook","secret":"your_secret_key","event_type":"order.created"}'
Ingest Webhook
bash
Copy
Edit
curl -X POST "http://localhost:8000/ingest/1" -H "Content-Type: application/json" -d '{"body":"payload_content","signature":"computed_signature"}'
Get Delivery Status
bash
Copy
Edit
curl "http://localhost:8000/status/{task_id}"
List Subscription Deliveries
bash
Copy
Edit
curl "http://localhost:8000/subscriptions/1/deliveries"
📈 Architecture Overview
plaintext
Copy
Edit
[Client] → [FastAPI Web Server] → [Redis Queue] → [Celery Workers]
                                    ↓
                               [PostgreSQL Logs]
⚡ Deployment
You can deploy easily to Render.com or Railway.app (both have free plans).

Use Docker deployment options.

Set environment variables for DATABASE_URL and REDIS_URL.

💵 Estimated Cost
PostgreSQL (Free Plan - 10k rows, 100MB) = $0

Redis (Free Plan) = $0

Render free dynos = $0

Total = $0/month for moderate traffic (~5,000 webhooks/day).

📋 Assumptions
Webhook targets are POST endpoints.

Secrets for signature verification are optional.

Basic payload format expected.

Event types are optional and filterable.

📢 Credits
FastAPI documentation

Celery documentation

Redis documentation

SQLAlchemy documentation

yaml
Copy
Edit

---

✅ **Done: README.md**

---

# 📢 How to Upload README.md

From your project root:

```bash
git add README.md
git commit -m "Add complete README documentation"
git push

