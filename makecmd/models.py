from django.db import models
from django.contrib.auth.models import User
class Mycmd(models.Model):
    product = models.CharField('product', max_length=250)
    prod_stat = models.CharField('prod_stat', max_length=100)
    cmded = models.BooleanField('cmded', default=False)
    received = models.BooleanField('received', default=False)
    indisponible = models.BooleanField('received', default=False)
    client = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


