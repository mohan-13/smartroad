from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

class user(models.Model):
    ROAD_OFFICER = 1
    SP = 1
    DRIVER = 0

    ACCOUNT_TYPES = (
        (ROAD_OFFICER, 'Road Officer'), (SP, 'SP'), (DRIVER, 'Driver'))
    base_user=models.ForeignKey(User,blank=True,null=True)
    user_type=models.IntegerField(blank=True,null=True,choices=ACCOUNT_TYPES)
    aadhar_id=models.CharField(max_length=12,unique=True,primary_key=True,default=0)
    fine=models.IntegerField(default=0)
    fine_date=models.DateTimeField(default=timezone.datetime.now())
class userdetails(models.Model):
    userid=models.ForeignKey(User,blank=True,null=True)
    licensenum=models.CharField(default=0,max_length=100)
    helmetid=models.IntegerField(default=0,blank=True,null=True)
class vehicledetails(models.Model):
    userid=models.ForeignKey(User,blank=True,null=True)
    regno=models.CharField(max_length=10,unique=True)
    insuranceid=models.CharField(max_length=50,blank=True,null=True)




# Create your models here.
