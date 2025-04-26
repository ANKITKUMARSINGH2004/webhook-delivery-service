from sqlalchemy import Column, Integer, String, Text, DateTime, JSON
from sqlalchemy.sql import func
from app.database import Base

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    target_url = Column(String, nullable=False)
    secret = Column(String, nullable=True)
    event_type = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class DeliveryLog(Base):
    __tablename__ = "delivery_logs"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(String, nullable=False)
    subscription_id = Column(Integer, nullable=False)
    target_url = Column(String, nullable=False)
    payload = Column(JSON, nullable=False)
    attempt_number = Column(Integer, default=1)
    status = Column(String, nullable=False)  # Success, Failed Attempt, or Failure
    status_code = Column(Integer, nullable=True)
    error_message = Column(Text, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
