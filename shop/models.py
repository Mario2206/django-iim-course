from django.db import models
from django.core import validators
from django.conf import settings
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField(validators=[validators.MinValueValidator(0)])
    quantity = models.IntegerField(validators=[validators.MinValueValidator(0)])
    image = models.FileField(upload_to="products")

    def __str__(self):
        return self.title
    
    def removeQuantity(self, quantity):
        self.quantity = self.quantity - quantity
        if self.quantity < 0 :
            self.quantity = 0
