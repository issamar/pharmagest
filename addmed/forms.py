from cProfile import label
from dataclasses import field


from django import forms
from .models import Addmed, Addart


class AddmedForm(forms.ModelForm):
    class Meta:
        model = Addmed
        fields = ['name', 'dci', 'dosage', 'cond']
        labels = {
            'name' : '',
            'dci' : '',
            'dosage' : '',
            'cond' : ''
           
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control text-uppercase autofocus', 
                'placeholder': 'Nom de produit et la forme galenique',
                'autocomplete' : 'autocomplete',
                'autofocus' : 'autofocus',
                'list' : 'meds'
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

        }

class AddartForm(forms.ModelForm):
    class Meta:
        model = Addart
        fields =[ 'full_name']
        labels = {
            'full_name' : ''
        }
        widgets = {
            'full_name' : forms.TextInput(attrs={
                'class' : 'form-control text-uppercase w-75 ',
                'placeholder' : "Nom d'article ou cosmetique ou complement alimentaire",
                'autocomplete' : 'autocomplete',
                'list' : 'arts'
            })
        }