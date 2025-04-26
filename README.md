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

2. **Set Environment Variables**
cp .env.example .env

