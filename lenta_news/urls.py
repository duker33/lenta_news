from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.NewsOrderForm.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^thanks/$', TemplateView.as_view(template_name='thanks.html')),
]
