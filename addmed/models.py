from django.db import models

# Create your models here.
class Addmed(models.Model):
    name = models.CharField('name', max_length=250)
    dci  = models.CharField('dci', max_length=250)
    dosage = models.CharField('dosage', max_length=50)
    cond = models.CharField('cond', max_length=100)
    

    def __str__(self):
        return self.name + ' ' + self.dosage + ' ' + self.cond 


class Addart(models.Model):
    full_name = models.CharField('full_name', max_length=300)

    def __str__(self):
        return self.full_name
   



        