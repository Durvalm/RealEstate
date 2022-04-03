from django.db import models

# Create your models here.


class Property(models.Model):
    objects = None
    property_type = models.CharField(max_length=100, blank=True)
    img = models.CharField(max_length=100000)
    price = models.IntegerField()
    description = models.CharField(max_length=100000)

