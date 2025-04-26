import json
from app.config import redis_client
from app import schemas
from typing import Optional

SUBSCRIPTION_CACHE_PREFIX = "subscription:"

def get_subscription(subscription_id: int) -> Optional[schemas.SubscriptionOut]:
    key = f"{SUBSCRIPTION_CACHE_PREFIX}{subscription_id}"
    cached = redis_client.get(key)
    if cached:
        data = json.loads(cached)
        return schemas.SubscriptionOut(**data)
    return None

def set_subscription(subscription):
    key = f"{SUBSCRIPTION_CACHE_PREFIX}{subscription.id}"
    data = {
        "id": subscription.id,
        "target_url": subscription.target_url,
        "secret": subscription.secret,
        "event_type": subscription.event_type,
        "created_at": str(subscription.created_at)
    }
    redis_client.set(key, json.dumps(data), ex=3600)  # Cache for 1 hour
