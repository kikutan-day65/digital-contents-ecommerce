from django.db import models
from users.models import Profile

# Create your models here.
class Product(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=False, blank=False)
    format = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default="default.jpg")
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return str(self.name)
    
class Tag(models.Model):
    tag_name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.tag_name)