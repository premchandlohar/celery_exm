import os

BROKER_USER = os.environ.get("BROKER_USER")
BROKER_PASSWORD = os.environ.get("BROKER_PASSWORD")
BROKER_HOST = os.environ.get("BROKER_HOST")
BROKER_PORT = os.environ.get("BROKER_PORT")
BROKER_VHOST = os.environ.get("BROKER_VHOST")

CELERY_BROKER_URL=f"amqp://{BROKER_USER}:{BROKER_PASSWORD}@{BROKER_HOST}:{BROKER_PORT}/{BROKER_VHOST}"
# 'django://'
BROKER_URL = 'django://'