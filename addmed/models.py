from django.db import models

# Create your models here.
class Addmed(models.Model):
    type_choices = [("MEDICAMENT", "MEDICAMENT"),("ARTICLE","ARTICLE")]
    name = models.CharField('name', max_length=250)
    dci  = models.CharField('dci', max_length=250)
    dosage = models.CharField('dosage', max_length=50)
    cond = models.CharField('cond', max_length=25)
    types = models.CharField('types', choices=type_choices, max_length=50)

    def __str__(self):
        return self.name + ' ' + self.dosage + ' ' + self.cond


        