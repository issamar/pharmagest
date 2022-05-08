import re
from traceback import print_tb
from urllib import request
from django.shortcuts import render
import itertools
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddmedForm, AddartForm
from .models import Addmed, Addart
# Create your views here.

# a function to add new product to the database
@login_required(login_url='main-page')
def AddMed(request): 
    form = AddmedForm()
    art_form = AddartForm()
    # pull all meds from db
    products = Addmed.objects.values_list('name', flat=True)
    products_list = list(itertools.chain(*products))
    dciss = list(Addmed.objects.values_list('dci', flat=True))
    dcis = set([a.strip(' ') for a in dciss])

    if request.method == 'POST':
        
        if 'med_btn' in request.POST:
            new_name = request.POST['name'].lower()
            form = AddmedForm(request.POST)
           
            if new_name not in products_list:
                if form.is_valid():
                    
                    form.save()
                    form = AddmedForm
                    messages.success(request, 'Produit Enregistrer avec succé')
            
            else:
                inserted_dosage = request.POST['dosage'].lower()
                inserted_cond = request.POST['cond'].lower()
                product_index = products_list.index(new_name)
                db_prod_dosage = products_list[product_index + 2]
                db_prod_cond = products_list[product_index + 3]
                
                if inserted_dosage != db_prod_dosage or inserted_cond != db_prod_cond:
                   
                    form.save()
                    form = AddmedForm
                else:
                    messages.error(request,'Ce produit existe deja')
                    
                    form = AddmedForm
        
        elif 'art_btn' in request.POST:
            new_name = request.POST['full_name'].lower()
            
            art_form = AddartForm(request.POST)
            all_arts = Addart.objects.values_list()
            arts_list = list(itertools.chain(*all_arts))
           
            if new_name not in arts_list:
                if art_form.is_valid():
                    
                    art_form.save()
                    art_form = AddartForm
                    messages.success(request, 'Produit Enregistrer avec succé')
            else:
                messages.warning(request,'Cet article existe deja')

        
        
    return render(request, 'addmed/add_med.html',{'form' : form, 'dcis' : dcis, 'art_form' : art_form, })

@login_required(login_url='main-page')
def dech(request):
            # pull all meds from db
    products = Addmed.objects.all()
    # products_list = list(itertools.chain(*products))
    arts = Addart.objects.all()



    if request.user_agent.is_pc:
        # pull all meds from db
        products = Addmed.objects.all()
    # products_list = list(itertools.chain(*products))
        
        arts = Addart.objects.all()
        prods =list(set( Addmed.objects.values_list('name', flat=True)))
        products_list = list(itertools.chain(*prods))
        dciss = list(Addmed.objects.values_list('dci', flat=True))
        clean_dcis = [a.strip(' ') for a in dciss]
        artss = Addart.objects.values_list('full_name', flat=True)
        arts_list = list(itertools.chain(*artss))
        
        if request.method =='POST':
            item_to_search = request.POST.get('dech')
            products_match = [ s for s in prods if item_to_search in s]
            dcis_match = [ s for s in set(clean_dcis) if item_to_search in s]
            arts_match = [ s for s in artss if item_to_search in s]
                

            return render (request, 'dech.html',{'products':products, 'arts':arts, 'products_match': products_match, 'dcis_match' : dcis_match, 'arts_match' : arts_match})



    if request.user_agent.is_mobile:
        if request.method =='POST':
            mob_prod = request.POST.get('search-field').lower()
            get_all_products = list(Addmed.objects.values_list('name', flat=True))
            get_all_dcis = list(Addmed.objects.values_list('dci', flat=True))
            clean_dcis = [a.strip(' ') for a in get_all_dcis]
            get_all_arts = list(Addart.objects.values_list('full_name', flat=True))

            matches_prod = list(filter(lambda x:mob_prod in x, get_all_products))
            matches_dci = list(filter(lambda y:mob_prod in y, set(clean_dcis)))
            matches_art = list(filter(lambda z:mob_prod in z, get_all_arts))
            
            return render(request, 'dech-mob.html',{'products':products, 'arts':arts,'matches_prod':matches_prod,'matches_dci':matches_dci,'matches_art':matches_art})
        return render(request, 'dech-mob.html',{'products':products, 'arts':arts,})
            
            
    return render (request, 'dech.html',{'products':products, 'arts':arts})