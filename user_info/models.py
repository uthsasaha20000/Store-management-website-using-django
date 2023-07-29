from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import AbstractUser

class User_infoo(models.Model):
    username=models.CharField(max_length=25,unique=True)
    email=models.EmailField(max_length=25,unique=True)
    password=models.CharField(max_length=50)
    age=models.IntegerField()
    city=models.CharField(max_length=25)
    gender= models.CharField(max_length=25)
    image=models.ImageField(upload_to="media/image/",null=True)
    #user_slug=AutoSlugField(populate_from="username",unique=True,null=True,default=None)
   
  


    
def __str__(self):
  return self.username