from django.db import models

# Create your models here.

class Contener(models.Model):
    name = models.TextField(max_length=100)
    size = models.FloatField()
    type = models.TextField()
    price = models.ForeignKey('Price', on_delete=models.CASCADE)

class Price(models.Model):
    price = models.IntegerField()
    description = models.TextField(max_length=100)
    update_date = models.DateField()