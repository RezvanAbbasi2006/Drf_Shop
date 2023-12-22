from config.settings import email
from django.core.mail import send_mail
from config.celery import app


@app.task()
def send_email_task(subject, message, recipient_list):
    email_from = email.EMAIL_HOST_USER
    send_mail(subject, message, email_from, recipient_list)


@app.task()
def test_task():
    print("this is test task")
    return "test task"
