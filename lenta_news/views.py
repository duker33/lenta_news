from django.shortcuts import render
from django.http import HttpResponseRedirect

from lenta_news.forms import OrderNewsForm
from lenta_news.services.mail_pdf import send_news_email


# TODO - throw CBV
def get_news_order(request):
    if request.method == 'POST':
        form = OrderNewsForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            date_to = form.cleaned_data['date_to']
            date_from = form.cleaned_data['date_from']
            result = send_news_email.delay(
                email_to=email,
                news_date_to=date_to,
                news_date_from=date_from
            )
            result.get()
            return HttpResponseRedirect('/thanks/')
    else:
        form = OrderNewsForm()

    return render(request, 'order_news.html', {'form': form})


def thanks_page(request):
    return render(request, 'thanks.html')
