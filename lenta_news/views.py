from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import OrderNewsForm


def get_news_order(request):
    if request.method == 'POST':
        form = OrderNewsForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            date_to = form.cleaned_data['date_to']
            date_from = form.cleaned_data['date_from']
            print(email, date_to, date_from)
            # TODO - redirect page
            return HttpResponseRedirect('/thanks/')
    else:
        form = OrderNewsForm()

    return render(request, 'order_news.html', {'form': form})


def thanks_page(request):
    return render(request, 'thanks.html')
