import imp 
import re
from django.shortcuts import render, redirect
from .models import Bordereaux
from .forms import BordereauxForm, EditBrdFrom
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import login_required
from mainpage.decorators import allowed_users
# Create your views here.

@login_required(login_url='main-page')
@allowed_users(allowed_roles=['admin'])
def brd(request):
	form = BordereauxForm(request.POST or None)
	all_brd = Bordereaux.objects.all().order_by('dt_clo')
	if request.method == 'POST':
		
		form = BordereauxForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Bordereau Ajouter Avec Succés')
			form = BordereauxForm()
	return render(request,'brd.html',{'form': form,'all_brd': all_brd})


@login_required(login_url='main-page')
@allowed_users(allowed_roles=['admin'])
def editBrd(request, pk):
	selected_brd = Bordereaux.objects.get(id = pk)
	form = EditBrdFrom(instance=selected_brd)
	if request.method == 'POST':
		n_ord = request.POST['n_ord']
		m_brd = request.POST['m_brd']
		n_jrl = request.POST['n_ord_jrl']
		m_jrl = request.POST['m_jrl']
		date_jrl = request.POST['dt_jrl']

		date1 = datetime.datetime.strptime(date_jrl, "%Y-%m-%d")
		date_pay = date1 + datetime.timedelta(days=15)
		selected_brd.defr = float(m_brd) - float(m_jrl)
		selected_brd.def_o = int(n_ord) - int(n_jrl)
		selected_brd.dt_pay = date_pay
		
		form = EditBrdFrom(request.POST,instance=selected_brd)
		if form.is_valid():
			
			form.save()
			form = EditBrdFrom()
			return redirect('brd')
	return render(request,"edit-brd.html",{'form': form})

@login_required(login_url='main-page')
@allowed_users(allowed_roles=['admin'])
def filterBrd(request):
	current_month = datetime.datetime.now().month
	current_year = datetime.datetime.now().year

	if request.method == 'POST':
		centre = request.POST['centre']
		period = request.POST['time']
		pay = request.POST['payement']
		


		
		# Ce mois
		if centre == 'Tous'and period == 'Ce mois' and pay == 'Tous' :
			
			data = Bordereaux.objects.filter(dt_clo__month = current_month, dt_clo__year = current_year)
			return render(request, 'brd.html',{'data': data})
		if centre == 'Tous'and period == 'Ce mois' and pay == 'Payé' :
			
			pay = True
			data = Bordereaux.objects.filter(dt_clo__month = current_month, dt_clo__year = current_year).filter(payement = pay)
			return render(request, 'brd.html',{'data': data})
		if centre == 'Tous'and period == 'Ce mois' and pay == 'Non Payé' :
			
			pay = False
			data = Bordereaux.objects.filter(dt_clo__month = current_month, dt_clo__year = current_year).filter(payement = pay)
			return render(request, 'brd.html',{'data': data})
		if period == "Ce mois" and pay == 'Non Payé':
			pay = False
			data = Bordereaux.objects.filter(pay_ctr = centre).filter(payement = pay).filter(dt_clo__month = current_month, dt_clo__year = current_year)
			
			return render(request, 'brd.html',{'data': data})
		if period == "Ce mois" and pay == 'Payé':
			pay = True
			data = Bordereaux.objects.filter(pay_ctr = centre).filter(payement = pay).filter(dt_clo__month = current_month, dt_clo__year = current_year)
			
			return render(request, 'brd.html',{'data': data})
		if period == "Ce mois" and pay == 'Tous':
			data = Bordereaux.objects.filter(pay_ctr = centre).filter(dt_clo__month = current_month, dt_clo__year = current_year)
			
			return render(request, 'brd.html',{'data': data})


		# Mois précédent
		if  period == "Mois précédent" and pay == 'Non Payé':
			pay = False
			if current_month == 1:
				current_month = 12
				current_year = current_year - 1
				data = Bordereaux.objects.filter(pay_ctr = centre).filter(payement = pay).filter(dt_clo__month = current_month, dt_clo__year = current_year)
				return render(request, 'brd.html',{'data': data})
			else:
				data = Bordereaux.objects.filter(pay_ctr = centre).filter(payement = pay).filter(dt_clo__month = current_month-1, dt_clo__year = current_year)
				return render(request, 'brd.html',{'data': data})
		if period == "Mois précédent" and pay == 'Tous':
			if current_month == 1:
				current_month = 12
				current_year = current_year - 1
				data = Bordereaux.objects.filter(pay_ctr = centre).filter(dt_clo__month = current_month, dt_clo__year = current_year)
				return render(request, 'brd.html',{'data': data})
			else:
				data = Bordereaux.objects.filter(pay_ctr = centre).filter(dt_clo__month = current_month-1, dt_clo__year = current_year)
				return render(request, 'brd.html',{'data': data})		
		if period == "Mois précédent" and pay == 'Payé':
			pay = True
			if current_month == 1:
				current_month = 12
				current_year = current_year - 1
				data = Bordereaux.objects.filter(pay_ctr = centre).filter(payement = pay).filter(dt_clo__month = current_month, dt_clo__year = current_year)
				return render(request, 'brd.html',{'data': data})
			else:
				data = Bordereaux.objects.filter(pay_ctr = centre).filter(payement = pay).filter(dt_clo__month = current_month-1, dt_clo__year = current_year)
				return render(request, 'brd.html',{'data': data})
		if centre == 'Tous'  and period == 'Mois précédent' and pay == 'Tous':
			if current_month == 1:
				current_month = 12
				current_year = current_year - 1
				print('helo', flush=True)
				data = Bordereaux.objects.filter(dt_clo__month = current_month-1, dt_clo__year = current_year)
				return render(request, 'brd.html',{'data': data})
			else:
				data = Bordereaux.objects.filter(dt_clo__month = current_month-1, dt_clo__year = current_year)

				return render(request, 'brd.html',{'data': data})
		if centre == 'Tous' and period == 'Mois précédent' and pay == 'Payé' :
			pay = True
			if current_month == 1:
				current_month = 12
				current_year = current_year - 1
				data = Bordereaux.objects.filter(dt_clo__month = current_month-1, dt_clo__year = current_year).filter(payement = pay)
				return render(request, 'brd.html',{'data': data})
			else:
				data = Bordereaux.objects.filter(dt_clo__month = current_month-1, dt_clo__year = current_year).filter(payement = pay)

				return render(request, 'brd.html',{'data': data})
		if centre == 'Tous' and period == 'Mois précédent' and pay == 'Non Payé' :
			pay = False
			if current_month == 1:
				current_month = 12
				current_year = current_year - 1
				data = Bordereaux.objects.filter(dt_clo__month = current_month-1, dt_clo__year = current_year).filter(payement = pay)
				return render(request, 'brd.html',{'data': data})
			else:
				data = Bordereaux.objects.filter(dt_clo__month = current_month-1, dt_clo__year = current_year).filter(payement = pay)

				return render(request, 'brd.html',{'data': data})
		
		
			return render(request, 'brd.html',{'data': data})
	return render(request, 'brd.html',{})


