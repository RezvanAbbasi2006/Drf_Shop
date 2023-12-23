from config.settings import email
from django.core.mail import send_mail
from config.celery import app
from celery.utils.log import get_logger

logger = get_logger(__name__)


@app.task()
def send_email(subject, message, recipient_list):
    try:
        email_from = email.EMAIL_HOST_USER
        send_mail(subject, message, email_from, recipient_list)
    except send_email.OperationalError as exc:
        logger.exception('Doing task error %r', exc)


@app.task()
def test_task():
    print("this is test task")
    return "test task"
