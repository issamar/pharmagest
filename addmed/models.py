from pyexpat import model
from django.db import models

# Create your models here.
class Addmed(models.Model):
    name = models.CharField('name', max_length=250)
    dci  = models.CharField('dci', max_length=250)
    dosage = models.CharField('dosage', max_length=50)
    cond = models.CharField('cond', max_length=100)
    tag = models.CharField('tag', max_length=1, default="M")

    def __str__(self):
        return self.name + ' ' + self.dosage + ' ' + self.cond

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        self.dci = self.dci.lower()
        self.dosage = self.dosage.lower()
        self.cond = self.cond.lower()
        return super(Addmed, self).save(*args, **kwargs) 


class Addart(models.Model):
    full_name = models.CharField('full_name', max_length=300)
    tag = models.CharField('tag', max_length=1, default="A")
    def __str__(self):
        return self.full_name
    def save(self, *args, **kwargs):
        self.full_name = self.full_name.lower()
        return super(Addart, self).save(*args, **kwargs) 
   



        