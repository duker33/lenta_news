from celery import shared_task
import xhtml2pdf.pisa as pisa
from io import StringIO, BytesIO

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template

from lenta_news.models import News


def render_news_to_pdf() -> bytes:
    """Get news from db and render it to pdf content"""
    template = get_template('pdf_news.html')
    html = template.render({'news_list': News.objects.all()})
    result = BytesIO()

    pdf = pisa.CreatePDF(StringIO(html), result)

    if pdf.err:
        raise IOError('pdf file creation failed!')
    file_content = result.getvalue()
    return file_content


@shared_task
def send_news_email(email_to, news_date_from, news_date_to):
    """Send email with attached news pdf"""
    news_content = render_news_to_pdf()
    message = EmailMessage(
        subject='Дайджест новостей',
        body='Дайджест новостей с lenta.ru за {}, {}'.format(
            news_date_from, news_date_to
        ),
        from_email=settings.EMAIL_SENDER,
        to=[email_to]
    )
    message.attach(settings.PDF_FILE_NAME, news_content, 'application/pdf')
    message.send()
