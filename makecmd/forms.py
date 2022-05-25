from cProfile import label
from dataclasses import field, fields
from random import choices


from django import forms
from .models import Mycmd


class MycmdForm(forms.ModelForm):
    class Meta:
        model = Mycmd
        fields = ['product', 'prod_stat', 'qtt','cmded', 'received', 'indisponible', 'client']
        widgets = {
            'client' : forms.Select(attrs={
            'type' : 'hidden',
            
                
                
            }),

            
        }

         

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Mycmd
        fields = ['product', 'prod_stat', 'qtt']
        choices = (('Pas de Stock','Pas de Stock'),('Faible Stock','Faible Stock'),('Pour Ord','Pour Ord'),('Quota', 'Quota'))
        widgets = {
            'product' : forms.TextInput(attrs={
                'class' : 'form-control',

            }),
            'prod_stat' : forms.Select(attrs={
                'class' : 'form-control',

            }, choices=choices),
            'qtt' : forms.TextInput(attrs={
                'class' : 'form-control',

            }),
        }