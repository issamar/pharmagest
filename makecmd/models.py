from django.db import models

class Mycmd(models.Model):
    product = models.CharField('product', max_length=250)
    prod_stat = models.CharField('prod_stat', max_length=100)
    cmded = models.BooleanField('cmded', default=False)
    received = models.BooleanField('received', default=False)
    
 
