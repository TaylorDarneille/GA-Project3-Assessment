from django.db import models

# Create your models here.
class Widget(models.Model):
    description = models.CharField(max_length=100)
    # missing parentheses on the .IntegerField method below
    # see docs: https://docs.djangoproject.com/en/3.0/topics/db/models/#fields
    # quantity = models.IntegerField
    quantity = models.IntegerField(default=1)