from unicodedata import category
from django.db import models

class Order(models.Model):
  name = models.CharField(max_length=32)
  phone = models.CharField(max_length=16)
  real_estate_agency = models.CharField(max_length=32)
  order_description = models.TextField(max_length=255)
  company = models.CharField(max_length=32)
  order_category = models.CharField(max_length=32)
  deadline = models.DateField()

  def __str__(self):
    return self.name
