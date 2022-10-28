from faulthandler import disable
from urllib import request
from django import forms

from .models import Closure


class ClosureForm(forms.ModelForm):
	
	class Meta:
		model = Closure
		fields = [
			'username',
			'start_money',
			'closure_money',
			'closure_paper',
			'money',
			'details',
			'wasfa'
		]


		widgets = {
			'username' : forms.Select(attrs={
				'id':'str_mny',
				'class' : 'form-control inpt',
				'Hidden' :'True'
				
				}),
			'start_money' : forms.NumberInput(attrs={
				'id':'str_mny',
				'class' : 'form-control inpt',
				'placeholder' : 'Argent Entrée'
				}),
			'closure_money' : forms.NumberInput(attrs={
				'id':'clo_mny',
				'class' : 'form-control inpt',
				'placeholder' : 'Argent Sortie'
				}),
			'closure_paper' : forms.NumberInput(attrs={
				'id':'clo_pper',
				'class' : 'form-control inpt',
				'placeholder' : 'Recette'
				}),
			'money' : forms.NumberInput(attrs={
				'id':'mny',
				'class' : 'form-control inpt',
				'placeholder' : 'Ecart'
				}),
			'details' : forms.TextInput(attrs={
				'id':'dtls',
				'class' : 'form-control inpt',
				'placehlder' : 'Details'
				}),
			'wasfa' : forms.TextInput(attrs={
				'id':'logi',
				'class' : 'form-control inpt',
				'placehlder' : 'Logiciel'
				}),



		}

		labels = {
			'username' : ("User"),
			'start_money' : ("Argent De Départ"),
			'closure_money' : ("Argent De Sortie"),
			'closure_paper' : ("Recette"),
			'money' : ("Ecart"),
			'details' : ("Details"),
			'wasfa' : ("Logiciel"),

		}





class PartielClosureForm(forms.ModelForm):
	class Meta:
		model = Closure
		fields = ['money', 'details']
		widgets = {
			'money' : forms.NumberInput(attrs={
				'id':'mny',
				'class' : 'input',
				'placeholder' : "La somme d'ecart"
				}),
			'details' : forms.TextInput(attrs={
				'id':'dtls',
				'class' : 'input',
				'placeholder' : "Details d'ecart"
				}),}