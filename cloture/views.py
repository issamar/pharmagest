from multiprocessing import context
from pickle import TRUE
from urllib import request
from django.shortcuts import render, redirect
from .forms import ClosureForm, PartielClosureForm
from .models import Closure
from django.contrib.auth.decorators import login_required
from mainpage.decorators import allowed_users
# Create your views here.

@login_required(login_url='main-page')
def closure(request):
	
	if request.method== "POST":
		post=request.POST.copy()
		post['username']=request.user
		request.POST = post
		
		form = ClosureForm(request.POST or None)
		
		if form.is_valid():

			form.save()
			
	last_id = Closure.objects.latest('id').pk
	last_start_money = Closure.objects.get(id = last_id).closure_money
	form = ClosureForm({'username':request.user, 'start_money':last_start_money})
	some_data = Closure.objects.all().order_by('-id')[:10]
	
	return render(request,'closure-page.html',{"form":form, 'datas' : some_data})



@login_required(login_url='main-page')
def editclo(request, pk):
	idid = Closure.objects.get(id=pk)
	form = PartielClosureForm(instance=idid)
	if request.method == 'POST':
		
		form  = PartielClosureForm(request.POST, instance=idid)
		if form.is_valid():
			form.save()
			
		return redirect('/cloture')

	context = {
		'form' : form
	}
	return render(request,'editclo.html', context)
@login_required(login_url='main-page')
@allowed_users(allowed_roles=['admin'])
def viewall(request):
	get_data = Closure.objects.all().order_by('-id')[:60]
	context = {
		'getdata' : get_data
	}
	return render(request,'viewall.html', context)

@login_required(login_url='main-page')
@allowed_users(allowed_roles=['admin'])
def editall(request, pk):
	row = Closure.objects.get(id=pk)
	form = ClosureForm(instance=row)
	if request.method == "POST":
		form  = ClosureForm(request.POST, instance=row)
		
		if form.is_valid():
			#get data one by one from the form before saving it
			cleaned_form = form.cleaned_data
			wasfa_amount = cleaned_form['wasfa']
			str_money = cleaned_form['start_money']
			clo_money = cleaned_form['closure_money']
			clo_paper = cleaned_form['closure_paper']
			ecart_money = cleaned_form['money']
			getdetail = cleaned_form['details']
			#calculate the real maney + Ecart
			real_mny = (clo_paper + clo_money) - str_money
			get_real_money = Closure.objects.get(id=pk)
			get_real_money.real_money= real_mny
			ecart_calc = (real_mny - wasfa_amount ) - ecart_money 
			#save edited data
			get_real_money.ecart = ecart_calc
			get_real_money.money = ecart_money
			get_real_money.details = getdetail
			get_real_money.wasfa = wasfa_amount
			form.save()
			get_real_money.save()

			return redirect('/cloture/viewall')
	context = {
		'form' : form
	}
	return render(request,'editall.html', context)
