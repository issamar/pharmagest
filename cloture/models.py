from email.policy import default
from urllib import request
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Closure(models.Model):
	creation_date = models.DateTimeField(auto_now_add=True)
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	start_money = models.IntegerField()
	closure_money = models.IntegerField()
	closure_paper = models.IntegerField()
	money = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True, default=0)
	details = models.CharField(max_length=200, blank=True, null=True)
	wasfa = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True, default=0)
	real_money = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True, default=0)
	ecart = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)