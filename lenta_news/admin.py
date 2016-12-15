from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    fields = ['date_published', 'title', 'description']
    list_display = ['date_published', 'title', 'description']

admin.site.register(News, NewsAdmin)
