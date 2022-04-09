from cProfile import label
from dataclasses import field
from socket import fromshare
from tkinter import Widget
from django import forms
from .models import Addmed


class AddmedForm(forms.ModelForm):
    class Meta:
        model = Addmed
        fields = ['name', 'dci', 'dosage', 'cond', 'types']
        labels = {
            'name' : '',
            'dci' : '',
            'dosage' : '',
            'cond' : '',
            'types' : ''
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control text-uppercase autofocus', 
                'placeholder': 'Nom de produit et la forme galenique',
                'autocomplete' : 'autocomplete',
                'autofocus' : 'autofocus'
                }),
            'dci' : forms.TextInput(attrs={
                'class' : 'form-control text-uppercase mt-3', 
                'placeholder' : 'DCI',
                'list' : 'product'
                }),
            'dosage' : forms.TextInput(attrs={
                'class' : 'form-control text-uppercase mt-3', 
                'placeholder' : 'Dosage'}),
            'cond' : forms.TextInput(attrs={
                'class' : 'form-control text-uppercase mt-3', 
                'placeholder' : 'Conditionement (example F/100ml B/30)'}),
            'types' : forms.Select(attrs={
                'class' : 'form-control mt-3', 
                'placeholder' : 'Type de produit'}),
        }