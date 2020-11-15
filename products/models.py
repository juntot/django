from django.db import models

# Create your models here.
class Product(models.Model):
    prodtitle = models.TextField(max_length=30)
    photo = models.ImageField(default='default.png')

    def __str__(self):
        return self.prodtitle