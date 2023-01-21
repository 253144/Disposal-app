from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.TextField(max_length=100)
    lname = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)

class Address(models.Model):
    street = models.TextField(max_length=100)
    house = models.TextField(max_length=10)
    apart = models.TextField(max_length=10)
    zip = models.TextField(max_length=6)
    city = models.TextField(max_length=100)