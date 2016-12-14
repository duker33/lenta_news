from django.db import models


class News(models.Model):
    date_published = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()
