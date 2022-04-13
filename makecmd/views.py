from django.contrib import messages
import itertools 
from django.shortcuts import render
from addmed.models import Addmed, Addart
from .models import Mycmd
from .forms import MycmdForm
# Create your views here.
def CmdPage(request):
    # pull data from db based on categories
    My_cmd_ste = Mycmd.objects.filter(prod_stat= 'Pas de Stock',received=False).order_by('product')
    My_cmd_stf = Mycmd.objects.filter(prod_stat= 'Faible Stock' ,received=False).order_by('product')
    My_cmd_ord = Mycmd.objects.filter(prod_stat= 'Pour Ord' ,received=False).order_by('product')
    My_cmd_q = Mycmd.objects.filter(prod_stat= 'Quota' ,received=False).order_by('product')
    #count data 
    count_ste = Mycmd.objects.filter(prod_stat= 'Pas de Stock',received=False).count()
    count_ord = Mycmd.objects.filter(prod_stat= 'Pour Ord',received=False).count()
    count_stf = Mycmd.objects.filter(prod_stat= 'Faible Stock',received=False).count()
    count_q = Mycmd.objects.filter(prod_stat= 'Quota',received=False).count()
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
            all_prod_cmd = Mycmd.objects.values_list('product').filter(received = False)
            new_product = request.POST['product']
            all_prod_cmd_list = list(itertools.chain(*all_prod_cmd))
            
            if new_product not in all_prod_cmd_list:
                
                form = MycmdForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.info(request,'Produit ajouté avec succé')
                else:
                    messages.warning(request, 'Le produit selectionné est deja ajouté')
        elif 'cmded' in request.POST:
            selected_prods = request.POST.getlist('products')
            for item in selected_prods:
                obj = Mycmd.objects.get(product=item, received = False)
                print(obj, flush=True)
                obj.cmded = True
                
                obj.save()
        elif 'rec' in request.POST:
            selected_prods = request.POST.getlist('products')
            for item in selected_prods:
                obj = Mycmd.objects.get(product=item, received = False)
                obj.received = True
                obj.save()
        elif 'indis' in request.POST:
            selected_prods = request.POST.getlist('products')
            for item in selected_prods:
                obj = Mycmd.objects.get(product=item, received = False)
                obj.indisponible = True
                obj.save()



    return render(request,'cmd_page.html',{'products': products, 'arts' : arts, 'My_cmd_ste' : My_cmd_ste, 'My_cmd_stf': My_cmd_stf, 'My_cmd_ord' : My_cmd_ord, 'My_cmd_q': My_cmd_q,
                    'ste_ord': ste_ord, 'stf_q' : stf_q})























