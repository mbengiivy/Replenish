from django.db import models

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

    def __str__(self):
        return f'{self.name}-{self.quantity}'

class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)