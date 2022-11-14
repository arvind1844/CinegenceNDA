from django.db import models

# # Create your models here.
class Staff(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    aadhar=models.PositiveBigIntegerField(null=True,blank=True)
    pan_number=models.CharField(max_length=100,null=True,blank=True)
    contact=models.PositiveBigIntegerField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True,max_length=100)
    image = models.ImageField(null=True,blank=True)
    nda=models.FileField(null=True,blank=True)
    date=models.DateField(null=True,blank=True,auto_now_add=True)

class Visitor(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    contact=models.PositiveBigIntegerField(null=True,blank=True)
    image = models.ImageField()
    nda=models.FileField(null=True,blank=True)
    date=models.DateField(null=True,blank=True,auto_now_add=True)

class Client(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    aadhar=models.PositiveBigIntegerField(null=True,blank=True)
    pan_number=models.CharField(max_length=100,null=True,blank=True)   
    email=models.EmailField(null=True,blank=True)
    image = models.ImageField()
    nda=models.FileField(null=True,blank=True)
    date=models.DateField(null=True,blank=True,auto_now_add=True)