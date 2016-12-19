from datetime import datetime
from celery import shared_task
import urllib.request
from xml.etree import ElementTree

from django.conf import settings

from lenta_news.models import News


def get_rss() -> str:
    with urllib.request.urlopen(settings.RSS_URL) as response:
        rss = response.read()
    return rss.decode()


@shared_task
def fetch_news():
    """
    This function is called as scheduled celery task.
    Schedule for this task should be setup from django admin ui:
    Link on celery doc: https://goo.gl/YqutLY
    """
    root = ElementTree.fromstring(get_rss())
    for article in root[0].findall('item'):
        News.objects.get_or_create(
            title=article.find('title').text,
            description=article.find('description').text,
            date_published=datetime.strptime(
                article.find('pubDate').text, '%a, %d %b %Y %H:%M:%S %z'
            )
        )
