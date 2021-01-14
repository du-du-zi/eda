from django.db import models

# Create your models here.
class Coffee(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(default="", max_length=30) # null = False면 not null
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)