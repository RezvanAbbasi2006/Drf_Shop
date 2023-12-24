from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.email')


app = Celery('drf-shop')
app.config_from_object("config.settings.celery_config", namespace="CELERY")

app.autodiscover_tasks()

app.conf.update(
    task_routes={
        "tasks.send_mail": "q1",
        "tasks.test_task": "q2"
    },
    task_annotations={
        "tasks.send_email": {"rate_limit": "10/m"}
    },
    enable_utc=True,
    timezone="UTC",
    broker_connection_retry_on_startup=True,
)
