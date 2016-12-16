from datetime import datetime
import urllib.request
from xml.etree import ElementTree
import xhtml2pdf.pisa as pisa
from io import StringIO, BytesIO

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template

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


# TODO - use type hints
def render_news_to_pdf():
    """Get news from db and render it to pdf content"""
    template = get_template('pdf_news.html')
    html = template.render({'news_list': News.objects.all()})
    result = BytesIO()

    pdf = pisa.CreatePDF(StringIO(html), result)

    # TODO - process pdf errors
    if pdf.err:
        raise Exception('Jesus! Pdf error!')
    file_content = result.getvalue()
    return file_content


def send_news_email(email_to, news_date_from, news_date_to):
    news_content = render_news_to_pdf()
    message = EmailMessage(
        subject='Дайджест новостей',
        body='Дайджест новостей с lenta.ru за {}, {}'.format(
            news_date_from, news_date_to
        ),
        from_email=settings.EMAIL_SENDER,
        to=[email_to]
    )
    message.attach('lenta_news.pdf', news_content, 'application/pdf')
    message.send()
