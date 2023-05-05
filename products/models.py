from django.db import models
from users.models import Profile

# Create your models here.
class Product(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=50, null=False, blank=False)
    product_format = models.CharField(max_length=50, null=False, blank=False)
    product_description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.product_name)