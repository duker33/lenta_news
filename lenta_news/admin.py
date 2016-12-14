from django.contrib import admin

from .models import News


class NewsAdmin(News):
    pass

admin.register(News, NewsAdmin)
