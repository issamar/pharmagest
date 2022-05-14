from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
class Mycmd(models.Model):
    product = models.CharField('product', max_length=250)
    prod_stat = models.CharField('prod_stat', max_length=100)
    qtt = models.IntegerField('qtt', null=True, blank=True, default=0)
    cmded = models.BooleanField('cmded', default=False)
    received = models.BooleanField('received', default=False)
    received_0 = models.IntegerField('received_0', default=0)
    indisponible = models.BooleanField('indisponible', default=False)
    client = models.ForeignKey(User, on_delete=models.CASCADE, default=1)




