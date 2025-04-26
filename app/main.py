from fastapi import FastAPI, HTTPException, BackgroundTasks
from app import models, crud, schemas, tasks, cache, utils
from app.database import engine, SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from app.config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Webhook Delivery Service")

# Allow all CORS (for testing UI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency: Get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/subscriptions/", response_model=schemas.SubscriptionOut)
def create_subscription(subscription: schemas.SubscriptionCreate, db: Session = next(get_db())):
    return crud.create_subscription(db, subscription)

@app.get("/subscriptions/{subscription_id}", response_model=schemas.SubscriptionOut)
def read_subscription(subscription_id: int, db: Session = next(get_db())):
    db_subscription = crud.get_subscription(db, subscription_id)
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription

@app.put("/subscriptions/{subscription_id}", response_model=schemas.SubscriptionOut)
def update_subscription(subscription_id: int, subscription: schemas.SubscriptionUpdate, db: Session = next(get_db())):
    return crud.update_subscription(db, subscription_id, subscription)

@app.delete("/subscriptions/{subscription_id}")
def delete_subscription(subscription_id: int, db: Session = next(get_db())):
    crud.delete_subscription(db, subscription_id)
    return {"message": "Subscription deleted"}

@app.post("/ingest/{subscription_id}")
def ingest_webhook(subscription_id: int, background_tasks: BackgroundTasks, payload: dict, db: Session = next(get_db()), event_type: str = None):
    subscription = cache.get_subscription(subscription_id) or crud.get_subscription(db, subscription_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")

    if subscription.secret:
        utils.verify_signature(subscription.secret, payload)

    if subscription.event_type and subscription.event_type != event_type:
        raise HTTPException(status_code=400, detail="Event type mismatch.")

    task_id = tasks.queue_delivery(subscription_id, payload, event_type)
    return {"message": "Webhook queued for delivery", "task_id": task_id}

@app.get("/status/{task_id}")
def get_delivery_status(task_id: str, db: Session = next(get_db())):
    return crud.get_delivery_status(db, task_id)

@app.get("/subscriptions/{subscription_id}/deliveries", response_model=List[schemas.DeliveryLogOut])
def get_subscription_deliveries(subscription_id: int, db: Session = next(get_db())):
    return crud.get_latest_deliveries(db, subscription_id)

