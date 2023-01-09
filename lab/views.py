
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

def display_detail(request, searched_date = date.today() ):
    print(request, flush=True)
    all_labs = Labo.objects.filter(dt=searched_date)
    patients = Patients.objects.all()
    parameters= Parameters.objects.all()
    
    prele_count = Labo.objects.filter(dt=searched_date).count()
    total_payement = Labo.objects.filter(dt=searched_date).aggregate(Sum('pay'))
    total_rest = Labo.objects.filter(dt=searched_date).aggregate(Sum('rest'))
    hba1c_free = Labo.objects.filter(dt=searched_date).filter(hba1c = 'True').count()
    return render(request, 'addp.html', {'patients' : patients, 'parameters' : parameters, 'all_labs' : all_labs,'prele_count':prele_count,
                    'total_payement':total_payement,'total_rest':total_rest,'hba1c_free':hba1c_free, 'searched_date':searched_date})

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
    print("2",request, flush=True)
    patient_name = request.POST['p_name']
    searched_date = request.POST['dt']
    if patient_name and searched_date:
        searched = Labo.objects.filter(p_name= request.POST['p_name'], dt= searched_date)
    elif patient_name:
        searched = Labo.objects.filter(p_name= request.POST['p_name'])
    elif searched_date:
        searched = Labo.objects.filter( dt= searched_date)
    patients = Patients.objects.all()
    parameters= Parameters.objects.all()
    d_patient = Labo.objects.values_list('p_name')
    prele_count = Labo.objects.filter(dt=searched_date).count()
    total_payement = Labo.objects.filter(dt=searched_date).aggregate(Sum('pay'))
    total_rest = Labo.objects.filter(dt=searched_date).aggregate(Sum('rest'))
    hba1c_free = Labo.objects.filter(dt=searched_date).filter(hba1c = 'True').count()

    
    

    return render(request,'addp.html',{'searched':searched,'patients':patients,'parameters':parameters,'d_patient':d_patient,
                    'prele_count':prele_count,'total_payement':total_payement,'total_rest':total_rest,'hba1c_free':hba1c_free, 'searched_date':searched_date})