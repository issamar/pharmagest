import imp
import re
from django.shortcuts import render, redirect
from .models import Bordereaux
from .forms import BordereauxForm, EditBrdFrom
from django.contrib import messages
import datetime
# Create your views here.


def brd(request):
	form = BordereauxForm(request.POST or None)
	all_brd = Bordereaux.objects.all().order_by('-dt_clo')[:15]
	if request.method == 'POST':
		form = BordereauxForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'Bordereau Ajouter Avec Succés')
			form = BordereauxForm()
	return render(request,'brd.html',{'form': form,'all_brd': all_brd})



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
		print(n_ord, m_brd,n_jrl,m_jrl, flush=True)
		form = EditBrdFrom(request.POST,instance=selected_brd)
		if form.is_valid():
			
			form.save()
			form = EditBrdFrom()
			return redirect('brd')
	return render(request,"edit-brd.html",{'form': form})