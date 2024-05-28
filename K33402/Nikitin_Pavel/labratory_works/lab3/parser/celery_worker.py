from celery import Celery

celery_app = Celery("tasks", broker="redis://redis:6379/0")

celery_app.config_from_object("celeryconfig")

celery_app.autodiscover_tasks(['parser'])
