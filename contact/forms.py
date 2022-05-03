from cProfile import label
from dataclasses import field, fields
from pyexpat import model

from django import forms
from .models import Contact 

class ContatForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets={

            'user_mail' : forms.EmailInput(attrs={
                'placeholder ' : "Email ",
                'class' : 'form-control w-50'
            }),
            'subject' : forms.TextInput(attrs={
                'placeholder ' : "Sujet ",
                'class' : 'form-control w-50'
            }),
            'text' : forms.Textarea(attrs={
                'placeholder ' : "Description ",
                'class' : 'form-control w-50'
            })
        }