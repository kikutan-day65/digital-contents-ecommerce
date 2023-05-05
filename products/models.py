from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50, null=False, blank=False)
    product_format = models.CharField(max_length=50, null=False, blank=False)
    product_description = models.CharField(max_length=1000, null=True, blank=True)