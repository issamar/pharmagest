from asyncore import read
from cProfile import label
from dataclasses import field, fields
from pyexpat import model

from tkinter import Widget
from django import forms
from .models import UserPayementStat, Account
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs={
                'class' : 'form-control my-2',
                'placeholder ' : "Votre nom d'utilisateur"
            }),
              'email' : forms.EmailInput(attrs={
                'class' : 'form-control my-2',
                'placeholder ' : "Votre mail"
            })
        }
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Mot de passe'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Confirmer le mot de passe'})



class UserProofForm(forms.ModelForm):
    class Meta:
        model = UserPayementStat
        fields = ['user_name','selected_offer', 'proof_of_payement']
        label = {
            
            'selected_offer' : "L'offre choisi",
            'proof_of_payement' : 'La preuve de payement'
        }
        widgets={
            
            'selected_offer' : forms.Select(attrs={
                'class'  : 'form-control m-3',
            }),
            
           
        }