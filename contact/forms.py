from cProfile import label
from dataclasses import field, fields
from pyexpat import model
from socket import fromshare
from tkinter import Widget
from django import forms
from .models import Contact

class ContatForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets={
            'user_name' : forms.TextInput(attrs={
                'placeholder ' : "Nom d'utilisateur ",
                'class' : 'form-control w-25'
            }),
            'user_mail' : forms.EmailInput(attrs={
                'placeholder ' : "Email ",
                'class' : 'form-control w-25'
            }),
            'subject' : forms.TextInput(attrs={
                'placeholder ' : "Sujet ",
                'class' : 'form-control w-25'
            }),
            'text' : forms.Textarea(attrs={
                'placeholder ' : "Description ",
                'class' : 'form-control w-50'
            })
        }