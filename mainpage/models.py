import email
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File
# Create your models here.




class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.CharField('region', max_length=10, choices=[('Centre', 'Centre'),('Est', 'Est'),('Ouest', 'Ouest'),('Sud','Sud')])

    def __str__(self):
        return self.user.username
    
        



class UserPayementStat(models.Model):
    user_name = models.CharField('user_name', max_length=50, null=True)
    selected_offer = models.CharField('offer', max_length=30, choices=(('Basic','Basic'),))
    proof_of_payement = models.ImageField(null=True, upload_to = "images/" )
    def __str__(self):
        return self.user_name
    
        # before saving the instance we’re reducing the image
    def save(self, *args, **kwargs):
        new_image = self.reduce_image_size(self.proof_of_payement)
        self.proof_of_payement = new_image
        super().save(*args, **kwargs)
    def reduce_image_size(self, proof_of_payement):
        print(proof_of_payement)
        img = Image.open(proof_of_payement)
        thumb_io = BytesIO()
        img.save(thumb_io, 'jpeg', quality=50)
        new_image = File(thumb_io, name=proof_of_payement.name)
        return new_image
    