
from dataclasses import fields
from webbrowser import get
from django.shortcuts import render, redirect,HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
import lab
from django.db.models import Sum, Avg, Min, Max, Count
from datetime import date
from .forms import  PatientInfo
from .models import Patients, Parameters, Labo
# Create your views here.
@login_required(login_url='main-page')

def display_detail(request ):
    
    
    all_labs = Labo.objects.all().order_by('-dt')[:20]
    patients = Patients.objects.all()
    parameters= Parameters.objects.all()
    
  
    return render(request, 'addp.html', {'patients' : patients, 'parameters' : parameters, 'all_labs' : all_labs})

@login_required(login_url='main-page')
def addP(request):

    if request.method == 'POST':
        
        analyse = Labo()
        analyse.p_name = request.POST.get('p_name')
        analyse.params = request.POST.get('selected_parameters')
        analyse.lab_price = request.POST.get('selected_parameters_price_lab')
        analyse.price = request.POST.get('price')
        analyse.pay = request.POST.get('pay')
        analyse.rest = request.POST.get('rest')
        if request.POST.get('hba1c') == 'on':
            analyse.hba1c = True
        else:
            analyse.hba1c = False
        analyse.info = request.POST.get('info')
        analyse.save()

      
    return redirect(display_detail)




@login_required(login_url='main-page')
def addpinfo(request):
    patient_form = PatientInfo()
    if request.method == "POST":
        form = PatientInfo(request.POST)
        if form.is_valid:
            form.save()
            return redirect('display_detail')


    return render(request, 'addpinfo.html', {'patient_form' : patient_form})

@login_required(login_url='main-page')
def editrest(request, pk):
    getPatient = Labo.objects.get(id = pk)
    if request.method == "POST":
        if request.POST['valid'] == 'Valider':
            print(request.POST, flush=True)
            price = request.POST.get('prix')
            pay = request.POST.get('payement')
            rest = request.POST.get('reste')
            getPatient.price = price
            getPatient.pay = pay
            getPatient.rest= rest
            if request.POST.get('recu') == 'on':
                getPatient.delevered = True
            else:
                getPatient.delevered = False
                
            getPatient.save()
            return redirect('add-P')
        if request.POST['valid'] == 'Annuler':
            print(request.POST, flush=True)
            return redirect('add-P')
        if request.POST['valid'] == 'Supprimé?':
            getPatient.delete()
            return redirect('add-P')


    return render(request, 'edit-rest.html',{'getPatient' : getPatient})
@login_required(login_url='main-page')
def searchP(request):
    
    patient_name = request.POST['p_name']
    searched_date1 = request.POST['dt1']
    searched_date2 = request.POST['dt2']
    
    if patient_name == '' and searched_date1 and searched_date2:
        data = Labo.objects.filter(dt__gte = searched_date1, dt__lte = searched_date2).order_by('-dt')
        data_count = data.count()
        data_pay = data.aggregate(pay__sum=Sum('pay'))
        data_rest = data.aggregate(Sum('rest'))
        data_hba1c = Labo.objects.filter(dt__gte = searched_date1, dt__lte = searched_date2, hba1c = True).count()
        return render(request,'addp.html',{'all_labs':data,'prele_count':data_count,'total_payement':data_pay,'total_rest':data_rest,'hba1c_free':data_hba1c})
    if patient_name =='' and searched_date1 and searched_date2 == '':
        data = Labo.objects.filter(dt = searched_date1).order_by('-dt')
        data_count = data.count()
        data_pay = data.aggregate(pay__sum=Sum('pay'))
        data_rest = data.aggregate(Sum('rest'))
        data_hba1c = Labo.objects.filter(dt__gte = searched_date1, dt__lte = searched_date2, hba1c = True).count()
        return render(request,'addp.html',{'all_labs':data,'prele_count':data_count,'total_payement':data_pay,'total_rest':data_rest,'hba1c_free':data_hba1c})
    if patient_name and searched_date1 == '' and searched_date2 =='':
        data = Labo.objects.filter(p_name__icontains = patient_name).order_by('-dt')
        data_count = data.count()
        data_pay = data.aggregate(pay__sum=Sum('pay'))
        data_rest = data.aggregate(Sum('rest'))
        data_hba1c = Labo.objects.filter(dt__gte = searched_date1, dt__lte = searched_date2, hba1c = True).count()
        return render(request,'addp.html',{'all_labs':data,'prele_count':data_count,'total_payement':data_pay,'total_rest':data_rest,'hba1c_free':data_hba1c})
    if patient_name and searched_date1 and searched_date2:
        data = Labo.objects.filter(p_name__icontains = patient_name,dt__gte = searched_date1, dt__lte = searched_date2).order_by('-dt')
        data_count = data.count()
        data_pay = data.aggregate(pay__sum=Sum('pay'))
        data_rest = data.aggregate(Sum('rest'))
        data_hba1c = Labo.objects.filter(dt__gte = searched_date1, dt__lte = searched_date2, hba1c = True).count()
        return render(request,'addp.html',{'all_labs':data,'prele_count':data_count,'total_payement':data_pay,'total_rest':data_rest,'hba1c_free':data_hba1c})
    if patient_name and searched_date1 and searched_date2 == '':
        data = Labo.objects.filter(p_name__icontains = patient_name,dt= searched_date1).order_by('-dt')
        data_count = data.count()
        data_pay = data.aggregate(pay__sum=Sum('pay'))
        data_rest = data.aggregate(Sum('rest'))
        data_hba1c = Labo.objects.filter(dt__gte = searched_date1, dt__lte = searched_date2, hba1c = True).count()
        return render(request,'addp.html',{'all_labs':data,'prele_count':data_count,'total_payement':data_pay,'total_rest':data_rest,'hba1c_free':data_hba1c})   
    patients = Patients.objects.all()
    parameters= Parameters.objects.all()

    return render(request,'addp.html',{})