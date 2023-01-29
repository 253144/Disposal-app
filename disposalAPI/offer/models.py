from django.db import models

# Create your models here.


class Container(models.Model):
    name = models.TextField(max_length=100)
    size = models.FloatField()
    type = models.TextField()
    price = models.ForeignKey('Price', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()


class Price(models.Model):
    price = models.IntegerField()
    description = models.TextField(max_length=100)
    update_date = models.DateField()

    def __str__(self) -> str:
        return '{}'.format(self.price)
