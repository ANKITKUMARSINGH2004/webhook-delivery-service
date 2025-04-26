from app.config import celery_app

# Import tasks to register them with Celery
import app.tasks

if __name__ == "__main__":
    celery_app.start()
