from traceback import print_tb
from django.shortcuts import render
import itertools
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
    products = Addmed.objects.values_list()
    products_list = list(itertools.chain(*products))
    dcis = Addmed.objects.values_list('dci', flat=True)


    if request.method == 'POST':
        #print(request.POST, flush=True)
        if 'med_btn' in request.POST:
            new_name = request.POST['name'].lower()
            form = AddmedForm(request.POST)
           
            if new_name not in products_list:
                if form.is_valid():
                    #print('we are in if' , flush=True)
                    form.save()
                    form = AddmedForm
                    messages.success(request, 'Produit Enregistrer avec succé')
            
            else:
                inserted_dosage = request.POST['dosage'].lower()
                inserted_cond = request.POST['cond'].lower()
                product_index = products_list.index(new_name)
                db_prod_dosage = products_list[product_index + 2]
                db_prod_cond = products_list[product_index + 3]
                #print(inserted_cond, inserted_dosage, db_prod_cond, db_prod_dosage, flush=True)
                if inserted_dosage != db_prod_dosage or inserted_cond != db_prod_cond:
                    #print('we are in else' , flush=True)
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
            print(arts_list, flush=True)
            if new_name not in arts_list:
                if art_form.is_valid():
                    
                    art_form.save()
                    art_form = AddartForm
                    messages.success(request, 'Produit Enregistrer avec succé')
            else:
                messages.warning(request,'Cet article existe deja')

        
        
    return render(request, 'add_med.html',{'form' : form, 'dcis' : dcis, 'art_form' : art_form})
