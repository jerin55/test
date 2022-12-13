from datetime import date
import email
from email import message
from MySQLdb import Date
from django.db import models

# Create your models here.

"""class ProductDetails(models.Model):
    product_name=models.CharField(max_length=255)
    description=models.TextField()
    quantity=models.IntegerField()
    price=models.IntegerField()"""


"""class EmployeDeatils(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    emailid=models.CharField(max_length=255)
    phone=models.IntegerField()"""

"""class StudentDetails(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    emailid=models.CharField(max_length=255)
    batch=models.CharField(max_length=255)"""

"""class StudentEmail(models.Model):
    name=models.CharField(max_length=255) 
    course=models.CharField(max_length=255)
    email=models.EmailField(max_length=25)   """    



class StudentList(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    address=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    genter=models.CharField(max_length=255)
    phone=models.IntegerField()
    qualification=models.CharField(max_length=255)
    join_date=models.DateField()  

class Product(models.Model):
    name=models.CharField(max_length=255)
    category=models.CharField(max_length=255)   
    price=models.FloatField(default=0.0)
    count=models.IntegerField(default=0)
    user_image=models.ImageField(upload_to="images/",null=True)











        


