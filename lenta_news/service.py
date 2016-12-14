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
        News.objects.create(
            title=article.find('title').text,
            description=article.find('description').text,
            date_published=article.find('pubDate').text
        )
