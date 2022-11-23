from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.title}{self.price}'


    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

