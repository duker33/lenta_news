import urllib.request
from xml.etree import ElementTree


def get_rss() -> str:
    with urllib.request.urlopen('https://lenta.ru/rss/articles') as response:
        rss = response.read()
    return rss.decode()


# TODO - use type hints
def build_pdf():
    root = ElementTree.fromstring(get_rss())
    doc_title = root[0].find('title').text
    for article in root[0].findall('item'):
        print(article.find('description').text)
