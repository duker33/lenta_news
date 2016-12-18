from celery import Celery

from lenta_news.services import send_news_email

celery_app = Celery('tasks', backend='rpc://', broker='amqp://guest:guest@localhost:5672//')


@celery_app.task
def send_mail_async(**kwargs):
    result = send_news_email.delay(**kwargs)
    result.get()
