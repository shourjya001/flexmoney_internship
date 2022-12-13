from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import *
from django.db.models.signals import post_save
### user:-
# first_name,last_name,username,password email
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    usernames=models.CharField(max_length=200)
    phoneno=models.CharField(max_length=150)
    pemail=models.EmailField(max_length=254)
    age=models.CharField(max_length=150)
    bithdate=models.CharField(max_length=150)
    address=models.CharField(max_length=500)
    healthinfo=models.CharField(max_length=500)
    lastfeesdate=models.CharField(max_length=500)
    validitydate=models.CharField(max_length=150)
    feespaid=models.CharField(max_length=1000)
    shift=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    def __str__(self):  # __str__
        return (self.user.username)

class Newsletter(models.Model):
    email=models.CharField(max_length=200)

class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=254)
    sub=models.CharField(max_length=500)
    msg=models.CharField(max_length=1000)

class Advertisements(models.Model):
    header = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    startdate = models.CharField(max_length=255)
    enddate = models.CharField(max_length=255)
    createdate = models.CharField(max_length=255)

class Feestrack(models.Model):
    name=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    time=models.CharField(max_length=150)
    amount=models.CharField(max_length=150)
    validitydate=models.CharField(max_length=150)
    batchselected=models.CharField(max_length=150)
    
class Instructor(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=150)
    desc=models.CharField(max_length=1000)
    qual=models.CharField(max_length=1000)
    link=models.URLField(max_length=500)