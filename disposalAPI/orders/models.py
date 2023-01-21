from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Order(models.Model):

    # Define choices
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', _('ACTIVE')
        ON_ITS_WAY = 'ON_ITS_WAY', _('ON_ITS_WAY')
        PLACED = 'PLACED', _('PLACED')
        COLLECT = 'COLLECT', _('COLLECT')
        COMPLETED = 'COMPLETED', _('COMPLETED')

    class Platnosc(models.TextChoices):
        UNPAID = 'UNPAID', _('UNPAID')
        PAID = 'PAID', _('PAID')

    order_status= models.TextField(
        max_length=15,
        choices=Status.choices,
        default=Status.ACTIVE)

    payment_status = models.TextField(
        max_length=15,
        choices=Platnosc.choices,
        default=Platnosc.UNPAID)

    order_date = models.DateField()
    collect_date = models.DateField()
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)


class OrderList(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    container = models.ForeignKey('offer.Container', on_delete=models.CASCADE)