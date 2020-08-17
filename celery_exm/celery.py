from __future__ import absolute_import, unicode_literals

import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_exm.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('celery_exm')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')#, namespace='CELERY')

app.conf.beat_schedule = {#for automatic executable program purpose use beat_schedule
    'every-15-seconds':{
        'task':'notification.tasks.send_email',
        'schedule':15,
        'args':('pythondjango19@gmail.com',)
    }
}
# app.config_from_object("celery_exm.config", namespace="CELERY")

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()
app.autodiscover_tasks(settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# from celery.schedules import crontab


# app.conf.beat_schedule = {
#     "trigger-email-notifications": {
#         "task": "notification.send_emails",
#         "schedule": crontab(minute="0", hour="0")
#     }
# }
