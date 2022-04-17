from http import client
from django.contrib import messages
import itertools 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from addmed.models import Addmed, Addart
from .models import Mycmd
from .forms import MycmdForm
# Create your views here.
@login_required(login_url='main-page')
def CmdPage(request):
    form = MycmdForm
    current_user = request.user.id
    print(current_user, flush=True)
    
    # pull data from db based on categories
    My_cmd_ste = Mycmd.objects.filter(prod_stat= 'Pas de Stock',received=False, client= current_user).order_by('product')
    My_cmd_stf = Mycmd.objects.filter(prod_stat= 'Faible Stock' ,received=False, client= current_user).order_by('product')
    My_cmd_ord = Mycmd.objects.filter(prod_stat= 'Pour Ord' ,received=False, client= current_user).order_by('product')
    My_cmd_q = Mycmd.objects.filter(prod_stat= 'Quota' ,received=False, client= current_user).order_by('product')
    #count data 
    count_ste = Mycmd.objects.filter(prod_stat= 'Pas de Stock',received=False, client= current_user).count()
    count_ord = Mycmd.objects.filter(prod_stat= 'Pour Ord',received=False, client= current_user).count()
    count_stf = Mycmd.objects.filter(prod_stat= 'Faible Stock',received=False, client= current_user).count()
    count_q = Mycmd.objects.filter(prod_stat= 'Quota',received=False, client= current_user).count()
    ste_ord = count_ord + count_ste
    stf_q = count_q + count_stf

    # get all the meds and arts to the datalist options
    #meds = Mycmd.objects.values_list('product')
    #for med in meds:
        #meds_list = list(med)
    
    products = Addmed.objects.all()
    arts = Addart.objects.all()
    # check validation & save the selected data
    if request.method == 'POST':
        
        if 'register' in request.POST:
            all_prod_cmd = Mycmd.objects.values_list('product').filter(received = False, client = current_user)
            new_product = request.POST['product']
            all_prod_cmd_list = list(itertools.chain(*all_prod_cmd))
            if new_product not in all_prod_cmd_list:
                
                form = MycmdForm(request.POST)
                
                if form.is_valid():
                   
                    form.save()

                    messages.info(request,'Produit ajouté avec succé')
                    ste_ord = count_ord + count_ste
                    stf_q = count_q + count_stf
                else:
                    messages.warning(request, 'Le produit selectionné est deja ajouté')
        elif 'cmded' in request.POST:
            selected_prods = request.POST.getlist('products')
            for item in selected_prods:
                obj = Mycmd.objects.get(product=item, received = False, client= current_user)
                print(obj, flush=True)
                obj.cmded = True
                
                obj.save()
        elif 'rec' in request.POST:
            selected_prods = request.POST.getlist('products')
            for item in selected_prods:
                obj = Mycmd.objects.get(product=item, received = False, client = current_user)
                obj.received = True
                obj.save()
        elif 'indis' in request.POST:
            selected_prods = request.POST.getlist('products')
            for item in selected_prods:
                obj = Mycmd.objects.get(product=item, received = False, client = current_user)
                obj.indisponible = True
                obj.save()
        My_cmd_ste = Mycmd.objects.filter(prod_stat= 'Pas de Stock',received=False, client= current_user).order_by('product')
        My_cmd_stf = Mycmd.objects.filter(prod_stat= 'Faible Stock' ,received=False, client= current_user).order_by('product')
        My_cmd_ord = Mycmd.objects.filter(prod_stat= 'Pour Ord' ,received=False, client= current_user).order_by('product')
        My_cmd_q = Mycmd.objects.filter(prod_stat= 'Quota' ,received=False, client= current_user).order_by('product')
        #count data 
        count_ste = Mycmd.objects.filter(prod_stat= 'Pas de Stock',received=False, client= current_user).count()
        count_ord = Mycmd.objects.filter(prod_stat= 'Pour Ord',received=False, client= current_user).count()
        count_stf = Mycmd.objects.filter(prod_stat= 'Faible Stock',received=False, client= current_user).count()
        count_q = Mycmd.objects.filter(prod_stat= 'Quota',received=False, client= current_user).count()
        ste_ord = count_ord + count_ste
        stf_q = count_q + count_stf

 
    return render(request,'cmd_page.html',{'form' : form, 'products': products, 'arts' : arts, 'My_cmd_ste' : My_cmd_ste, 'My_cmd_stf': My_cmd_stf, 'My_cmd_ord' : My_cmd_ord, 'My_cmd_q': My_cmd_q,
                    'ste_ord': ste_ord, 'stf_q' : stf_q , 'current_user'  : current_user})























