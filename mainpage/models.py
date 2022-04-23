import email
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.CharField('region', max_length=10, choices=[('Centre', 'Centre'),('Est', 'Est'),('Ouest', 'Ouest'),('Sud','Sud')])

    def __str__(self):
        return self.user.username
