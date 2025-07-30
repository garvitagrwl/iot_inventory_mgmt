from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE



class Student(models.Model):
    full_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=50, unique=True)
    college_email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    password =  models.CharField(max_length=15,blank=True)


    def __str__(self):
        return self.full_name
