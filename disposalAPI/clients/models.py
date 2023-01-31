from django.db import models
import json

# Create your models here.


class Client(models.Model):
    name = models.TextField(max_length=100)
    lname = models.TextField(max_length=100)
    phone = models.TextField(max_length=100)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return json.dumps({'name': '{}'.format(self.name)})


class Address(models.Model):
    street = models.TextField(max_length=100)
    house = models.TextField(max_length=10)
    apart = models.TextField(max_length=10)
    zip = models.TextField(max_length=6)
    city = models.TextField(max_length=100)

    def __str__(self) -> str:
        if self.apart == None:
            return '{} {}, {} {}'.format(self.street, self.house, self.zip, self.city)
        else:
            return '{} {}/{}, {} {}'.format(self.street, self.house, self.apart, self.zip, self.city)
