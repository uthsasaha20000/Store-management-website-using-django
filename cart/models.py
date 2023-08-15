from django.db import models

# Create your models here.
class Cart(models.Model):
    name=models.CharField(max_length=25,unique=True)
    p_name=models.CharField(max_length=25,unique=True)
    unit=models.IntegerField()
    amount=models.IntegerField()