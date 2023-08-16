from django.db import models

# Create your models here.
class Cart(models.Model):

    p_name=models.CharField(max_length=25,unique=True)
  