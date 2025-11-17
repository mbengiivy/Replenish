from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name


class Order(models.Model):
    name = models.CharField(max_length=200)
    order_quantity = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name