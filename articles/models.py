from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(this):
        return this.title