from django.db import models

# Create your models here.
class RegisterUser(models.Model):
    fname=models.CharField( max_length=50)
    lname=models.CharField( max_length=50)
    uname=models.CharField( max_length=50)
    email=models.EmailField( max_length=154)
    password=models.CharField(max_length=50)
  