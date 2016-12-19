# this code - copy of example:
# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lenta_news.settings')

app = Celery('lenta_news', backend='rpc://', broker='amqp://guest:guest@localhost:5672//')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
