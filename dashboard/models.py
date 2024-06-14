from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY = (
    ('Birthday','Birthday'),
    ('Baby Shower','Baby Shower'),
    ('Gender Reveal','Gender Reveal'),
    ('Decor','Decor'),
    ('Toys','Toys'),
    ('Board Games','Board Games')

)
class Product(models.Model):
    name= models.CharField(max_length=50, null=True)
    code=models.CharField(max_length=10, null=True)
    category=models.CharField(max_length=50, choices=CATEGORY)
    quantity=models.PositiveBigIntegerField(null=True)
    price=models.PositiveBigIntegerField(null=True)

    class Meta:
        verbose_name_plural='Product'

    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, models.CASCADE, null = True)
    order_quantity= models.PositiveIntegerField(null = True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Order'
        #To bring a singular form to the admin side
    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}-{self.order_quantity}'
    