from cProfile import label
from dataclasses import field, fields
from socket import fromshare
from tkinter import Widget
from django import forms
from .models import Mycmd


class MycmdForm(forms.ModelForm):
    class Meta:
        model = Mycmd
        fields = '__all__'
   
         