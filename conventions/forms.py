from django import forms

from .models import Bordereaux



		
class BordereauxForm(forms.ModelForm):
	class Meta:
		model = Bordereaux
		fields = ['pay_ctr','n_brd','dt_clo','n_ord','m_brd','dt_depot']
		CTR_CHOICES = (
			('', ''),
			('CNAS','CNAS'),
			('CASNOS','CASNOS'),
			('Caisse Militaire','Caisse Militaire'))
		widgets = {
			'pay_ctr' : forms.Select(choices=CTR_CHOICES, attrs={
				'id' : 'ctr',
				'class' : 'form-control inpt',
				'title' : 'Centre de Payment'
				}),
			'n_brd' : forms.NumberInput(attrs={
				'id' : 'nbrd',
				'class' : 'form-control inpt',
				'placeholder' : 'N° Brd'
				}),
			'dt_clo' : forms.DateInput(attrs={
				'id' : 'dt_clo',
				'class' : 'form-control inpt',
				'title' : 'Date de cloture',
				'type' : 'date'
				}),
			'n_ord' : forms.NumberInput(attrs={
				'id' : 'nord',
				'class' : 'form-control inpt',
				'placeholder' : 'N° Ord'
				}),
			'm_brd' : forms.NumberInput(attrs={
				'id' : 'mbrd',
				'class' : 'form-control inpt',
				'placeholder' : 'Montant Brd'
				}),
			'dt_depot' : forms.DateInput(attrs={
				'id' : 'dtdepot',
				'class' : 'form-control inpt',
				'type' : 'date',
				'required' : 'True',
                'title' : 'Date de Depot'
				}),
		}
		labels = {
			'pay_ctr' : ("Payement center"),
			'n_brd' : ("Slip Number : "),
			'dt_clo' : (" Slip Closing Date"),
			'n_ord' : ("Prescription Number (Slip)"),
			'm_brd' : ("Slip Amount"),
			'dt_depot' : ("Diposit Date(Slip)"),
			# 'dt_jrl' : ("Date du Journal"),
			# 'n_ord_jrl' : ("Nombre d'Ordenance du Journal"),
			# 'm_jrl' : ("Montant du Journal")


		}


class EditBrdFrom(forms.ModelForm):
	class Meta:
		model = Bordereaux
		fields = ['pay_ctr', 'n_brd', 'dt_clo', 'n_ord','m_brd', 'dt_depot', 'dt_jrl', 'n_ord_jrl', 'm_jrl', "payement"]
		CTR_CHOICES = (
			('', ''),
			('CNAS','CNAS'),
			('CASNOS','CASNOS'),
			('Caisse Militaire','Caisse Militaire'))
		widgets = {
			'pay_ctr' : forms.Select(choices=CTR_CHOICES, attrs={
				'id' : 'ctr',
				'class' : 'form-control',
				}),
			'n_brd' : forms.NumberInput(attrs={
				'id' : 'nbrd',
				'class' : 'form-control',
				}),
			'dt_clo' : forms.DateInput(attrs={
				'id' : 'dt_clo',
				'type' : 'date',
				'class' : 'form-control',
				}),
			'n_ord' : forms.NumberInput(attrs={
				'id' : 'nord',
				'class' : 'form-control',
				}),
			'm_brd' : forms.NumberInput(attrs={
				'id' : 'mbrd',
				'class' : 'form-control',
				}),
			'dt_depot' : forms.DateInput(attrs={
				'id' : 'dtdepot',
				'type' : 'date',
				'class' : 'form-control',
				}),
			'dt_jrl' : forms.DateInput(attrs={
				'id' : 'dt_jrl',
				'type' : 'date',
				'class' : 'form-control',
				'required' : 'True'
 				}),
			'n_ord_jrl' : forms.NumberInput(attrs={
				'id' : 'n_ord_jrl',
				'class' : 'form-control',
	
				}),
			'm_jrl' : forms.NumberInput(attrs={
				'id' : 'm_jrl',
				'class' : 'form-control',

				})
			}
		labels = {
			'pay_ctr' : ("Payement center"),
			'n_brd' : ("Slip Number : "),
			'dt_clo' : (" Slip Closing Date"),
			'n_ord' : ("Prescription Number (Slip)"),
			'm_brd' : ("Slip Amount"),
			'dt_depot' : ("Diposit Date(Slip)"),
			'dt_jrl' : ("Sheet Date"),
			'n_ord_jrl' : ("Prescription Number(Sheet)"),
			'm_jrl' : ("Sheet Amount"),
			'payement': ('Payed?...')


		}

