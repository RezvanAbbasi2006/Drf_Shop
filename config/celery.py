from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.django")

app = Celery('drf-shop')
app.config_from_object("config.settings.celery", namespace="CELERY")

app.autodiscover_tasks()

app.conf.update(
    task_routes={
        "tasks.send_mail_to_users": "q1",
        "tasks.test_task": "q2"
    },
    task_annotations={"tasks.example_schedule_task": {"rate_limit": "10/m"}},
    enable_utc=True,
    timezone="UTC",
    broker_connection_retry_on_startup=True,
)
