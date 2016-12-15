from datetime import datetime
import urllib.request
from xml.etree import ElementTree

from .models import News


def get_rss() -> str:
    with urllib.request.urlopen('https://lenta.ru/rss/articles') as response:
        rss = response.read()
    return rss.decode()


def save_news_to_db():
    root = ElementTree.fromstring(get_rss())
    for article in root[0].findall('item'):
        News.objects.get_or_create(
            title=article.find('title').text,
            description=article.find('description').text,
            date_published=datetime.strptime(
                article.find('pubDate').text, '%a, %d %b %Y %H:%M:%S %z'
            )
        )
