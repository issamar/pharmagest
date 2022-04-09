from django.shortcuts import render
import itertools
from django.contrib import messages
from .forms import AddmedForm
from .models import Addmed
# Create your views here.

# a function to add new product to the database
def AddMed(request):
    form = AddmedForm()
    products = Addmed.objects.values_list()
    products_list = list(itertools.chain(*products))

    dcis = Addmed.objects.values_list('dci', flat=True)
    if request.method == 'POST':
        new_name = request.POST['name'].lower()
        form = AddmedForm(request.POST)
        if new_name not in products_list:
            if form.is_valid():
                print('we are in if' , flush=True)
                form.save()
                form = AddmedForm
        
        else:
            inserted_dosage = request.POST['dosage'].lower()
            inserted_cond = request.POST['cond'].lower()
            product_index = products_list.index(new_name)
            db_prod_dosage = products_list[product_index + 2]
            db_prod_cond = products_list[product_index + 3]
            print(inserted_cond, inserted_dosage, db_prod_cond, db_prod_dosage, flush=True)
            if inserted_dosage != db_prod_dosage or inserted_cond != db_prod_cond:
                print('we are in else' , flush=True)
                form.save()
                form = AddmedForm
            else:
                messages.error(request,'Ce produit existe deja')
                
                form = AddmedForm
             

        
        
    return render(request, 'add_med.html',{'form' : form, 'dcis' : dcis})
