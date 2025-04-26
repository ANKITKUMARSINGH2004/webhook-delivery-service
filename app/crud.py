from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy import desc
from typing import List

def create_subscription(db: Session, subscription: schemas.SubscriptionCreate):
    db_subscription = models.Subscription(**subscription.dict())
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

def get_subscription(db: Session, subscription_id: int):
    return db.query(models.Subscription).filter(models.Subscription.id == subscription_id).first()

def update_subscription(db: Session, subscription_id: int, subscription: schemas.SubscriptionUpdate):
    db_subscription = get_subscription(db, subscription_id)
    if not db_subscription:
        return None
    for var, value in vars(subscription).items():
        setattr(db_subscription, var, value) if value else None
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

def delete_subscription(db: Session, subscription_id: int):
    db_subscription = get_subscription(db, subscription_id)
    if db_subscription:
        db.delete(db_subscription)
        db.commit()

def log_delivery_attempt(db: Session, delivery_data: dict):
    db_log = models.DeliveryLog(**delivery_data)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_delivery_status(db: Session, task_id: str):
    return db.query(models.DeliveryLog).filter(models.DeliveryLog.task_id == task_id).order_by(desc(models.DeliveryLog.attempt_number)).first()

def get_latest_deliveries(db: Session, subscription_id: int) -> List[models.DeliveryLog]:
    return db.query(models.DeliveryLog).filter(models.DeliveryLog.subscription_id == subscription_id).order_by(desc(models.DeliveryLog.timestamp)).limit(20).all()

def delete_old_logs(db: Session, hours: int = 72):
    from datetime import datetime, timedelta
    cutoff = datetime.utcnow() - timedelta(hours=hours)
    db.query(models.DeliveryLog).filter(models.DeliveryLog.timestamp < cutoff).delete()
    db.commit()
