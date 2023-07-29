from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=25,unique=True)
    price=models.IntegerField()
    product_image=models.ImageField(upload_to="media/product_image/",null=True)
    catagory=models.CharField(max_length=25,unique=True)