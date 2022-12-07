from distutils.command.upload import upload
from itertools import product
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
class Mycmd(models.Model):
    product = models.CharField('product', max_length=250)
    prod_stat = models.CharField('prod_stat', max_length=100)
    qtt = models.IntegerField('qtt',default=0)
    cmded = models.BooleanField('cmded', default=False)
    received = models.BooleanField('received', default=False)
    received_0 = models.IntegerField('received_0', default=0)
    indisponible = models.BooleanField('indisponible', default=False)
    deleted = models.BooleanField('deleted', default=False)
    client = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    

 

class StatTable(models.Model):
    product = models.CharField('product', max_length=250)
    cmded = models.IntegerField('cmded', null=True)
    received = models.IntegerField('received', null=True)
    indisponible = models.IntegerField('indisponible', null=True)
   
