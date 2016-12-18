from django.shortcuts import render
from django.http import HttpResponseRedirect

from lenta_news.forms import OrderNewsForm
from lenta_news.services import send_mail_async


# TODO - throw CBV
def get_news_order(request):
    if request.method == 'POST':
        form = OrderNewsForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            date_to = form.cleaned_data['date_to']
            date_from = form.cleaned_data['date_from']
            send_mail_async(
                email_to=email,
                news_date_to=date_to,
                news_date_from=date_from
            )
            return HttpResponseRedirect('/thanks/')
    else:
        form = OrderNewsForm()

    return render(request, 'order_news.html', {'form': form})


def thanks_page(request):
    return render(request, 'thanks.html')
