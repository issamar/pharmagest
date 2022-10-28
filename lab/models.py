from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Labo(models.Model):
	dt = models.DateField(auto_now_add = True)
	p_name = models.CharField(max_length = 200)

	params = models.TextField(max_length=500)
	lab_price = models.IntegerField(default = 0)
	price = models.IntegerField(default = 0)
	pay = models.IntegerField(default = 0)
	rest = models.IntegerField(default=0)
	hba1c = models.BooleanField(default=False)
	info = models.TextField(max_length=200, blank = True)
	delevered = models.BooleanField(default=False)



class Parameters(models.Model):
    Param_name = models.CharField('parameter', max_length=500)
    lab_price = models.IntegerField(default=0)
    ph_price = models.IntegerField(default=0)



class Patients(models.Model):
    patient_name = models.CharField('name', max_length=250)
    patient_age = models.IntegerField('age')
    patient_dob = models.DateField('dob', blank=True, null = True)
    
