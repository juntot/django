from django.db import models
from djongo import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40, default=None)
    description = models.TextField()


    def __str__(this):
        return this.title

    def excerpt(this):
        return this.description[: 8]