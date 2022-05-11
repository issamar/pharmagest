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
    
        



class UserPayementStat(models.Model):
    user_name = models.CharField('user_name', max_length=50, null=True)
    selected_offer = models.CharField('offer', max_length=30, choices=(('Basic','Basic'),('Avancé','Avancé'),('Professionnel', 'Professionnel')))
    proof_of_payement = models.ImageField(null=True, upload_to = "images/" )
    def __str__(self):
        return self.user_name 
    