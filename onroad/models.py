from django.db import models
from django.utils import timezone
class checkdetails(models.Model):
    checked_by=models.CharField(max_length=12,default=0)
    driver=models.CharField(max_length=12,default=0)
    checked_on=models.DateTimeField(default=timezone.datetime.now())
    fine_imp=models.IntegerField(default=0)
    fine_reason=models.CharField(max_length=500,default="NILL")

# Create your models here.
