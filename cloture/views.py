from multiprocessing import context
from pickle import TRUE
from urllib import request
from django.shortcuts import render, redirect
from .forms import ClosureForm, PartielClosureForm
from .models import Closure
# Create your views here.


def closure(request):
	
	if request.method== "POST":
		post=request.POST.copy()
		post['username']=request.user
		request.POST = post
		print(request.POST, flush=True)
		form = ClosureForm(request.POST or None)
		
		if form.is_valid():

			form.save()
			print('done', flush=True)
		else:
			print('looooser', flush=True)
	form = ClosureForm({'username':request.user})
	some_data = Closure.objects.all().order_by('-id')[:10]
	
	return render(request,'closure-page.html',{"form":form, 'datas' : some_data})




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

def viewall(request):
	get_data = Closure.objects.all().order_by('-id')[:60]
	context = {
		'getdata' : get_data
	}
	return render(request,'viewall.html', context)


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
