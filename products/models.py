#from tabnanny import verbose
from django.db import models
#from django.forms import DateField

class Products(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    stock = models.IntegerField()
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
#para que ponga en display el nombre
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = 'Products'

class Category(models.Model):
    name = models.CharField(max_length=50)
