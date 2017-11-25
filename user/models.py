from django.contrib.auth.models import User
from django.db import models

from kompany.models import Products


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Cart"


class Orders(models.Model):
    order_date = models.DateTimeField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.CharField(default='', max_length=210)


class Addressbook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house_number = models.CharField(default='', max_length=250)
    locality = models.CharField(default='', max_length=250)
    region = models.CharField(default='', max_length=250)
    postcode = models.CharField(default='', max_length=250)
    country = models.CharField(default='', max_length=50)
