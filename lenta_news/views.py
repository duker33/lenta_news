from django.views.generic.edit import FormView

from lenta_news.forms import OrderNewsForm
from lenta_news.services.mail_pdf import send_news_email


class NewsOrderForm(FormView):
    template_name = 'order_news.html'
    form_class = OrderNewsForm
    success_url = '/thanks/'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        date_to = form.cleaned_data['date_to']
        date_from = form.cleaned_data['date_from']
        send_news_email.delay(
            email_to=email,
            news_date_to=date_to,
            news_date_from=date_from
        )
        return super(FormView, self).form_valid(form)
