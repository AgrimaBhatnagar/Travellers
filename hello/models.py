from django.db import models
from django.db.models.fields import DateField, EmailField

#
class Ccustum(models.Model):
    name=models.CharField(max_length=120 )
    phone=models.CharField(max_length=12)
    email=models.EmailField()
    password=models.CharField(max_length=12)
    flighttakeofflocation=models.CharField(max_length=100)
    flightlandonlocation=models.CharField(max_length=100)
    duration=models.CharField(max_length=20, default= '7 days')
    hotels=models.CharField(max_length= 500, )
    
    def __str__(self) -> str:
        return self.name 
       
