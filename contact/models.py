from re import MULTILINE
from statistics import mode
from django.db import models

# Create your models here.


class Contact(models.Model):
    user_name = models.CharField('user_name', max_length=50)
    user_mail = models.EmailField()
    subject = models.CharField('subject', max_length=250)
    text = models.TextField(max_length=500)
    def __str__(self):
        return self. user_name + ' ' + self.subject