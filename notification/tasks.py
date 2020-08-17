from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery_exm.celery import app
from notification.models import Userprofile

@shared_task
def sum(a,b):
    import time
    time.sleep(10)
    return a+b

@shared_task
def send_email(email):
    print(f'a sample msg is send to {email}')


# @app.task(name="notification.send_emails")
# def send_email_task():
#     """Task that send email to all users"""
#     users = User.objects.all()
#     send_user_emails(users=users)