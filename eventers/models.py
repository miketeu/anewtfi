from django.db import models

# Create your models here.
class Eventers(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    organisation = models.CharField(max_length=255)
    nameofevent = models.CharField(max_length=255)
    eventdetails = models.CharField(max_length=1000)
    eventfund = models.IntegerField(null=True)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
