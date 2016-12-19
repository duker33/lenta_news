from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['date_published', 'title', 'description']

admin.site.register(News, NewsAdmin)
