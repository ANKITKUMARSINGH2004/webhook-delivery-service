from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict
from datetime import datetime

class SubscriptionBase(BaseModel):
    target_url: HttpUrl
    secret: Optional[str] = None
    event_type: Optional[str] = None

class SubscriptionCreate(SubscriptionBase):
    pass

class SubscriptionUpdate(SubscriptionBase):
    pass

class SubscriptionOut(SubscriptionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class DeliveryLogOut(BaseModel):
    id: int
    task_id: str
    subscription_id: int
    target_url: str
    attempt_number: int
    status: str
    status_code: Optional[int] = None
    error_message: Optional[str] = None
    timestamp: datetime

    class Config:
        orm_mode = True
