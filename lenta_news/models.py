from django.db import models


class News(models.Model):
    date_published = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'news'
