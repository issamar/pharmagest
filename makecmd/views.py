from http import client
from django.contrib import messages
import itertools 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from addmed.models import Addmed, Addart
from .models import Mycmd, StatTable
from .forms import EditItemForm, MycmdForm
from datetime import datetime, timezone
from django.contrib.auth.models import User
from mainpage.decorators import loged_users, allowed_users

from django .db.models import F
# Create your views here. 
@login_required(login_url='main-page')
def CmdPage(request):
    
    form = MycmdForm
    current_user = request.user.id
    current_username = request.user
        
        
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
            else:
                messages.warning(request, 'Produit Existe Deja')
                new_product_db = Mycmd.objects.get(product = new_product).pk
                return redirect(editItem,prod_id = new_product_db)
                
                


        elif 'cmded' in request.POST:
            selected_prods = request.POST.getlist('products')
            for item in selected_prods:
                obj = Mycmd.objects.get(product=item, received = False)
                obj.cmded = True
                obj.save()
        elif 'rec' in request.POST:
            selected_prods = request.POST.getlist('products')
            for item in selected_prods:
                obj = Mycmd.objects.get(product=item, received = False)
                obj.received = True
                obj.received_0 = True
                obj.save()
                if obj.received == True:
                    get_all_deleted_item = list(StatTable.objects.values_list('product', flat=True))
                    
                    if item not in get_all_deleted_item:
                        new_item=StatTable.objects.create(product = item)
                        new_item.cmded = 1
                        new_item.received = 1
                        new_item.indisponible = 0
                        new_item.save()
                        Mycmd.objects.get(product=item, received = True, deleted=False).delete()
                    elif item in get_all_deleted_item:
                        exiting_item = StatTable.objects.filter(product = item).update(cmded = F('cmded') + 1, received=F('received') + 1)
                        Mycmd.objects.get(product=item, received = True, deleted=False).delete()
        elif 'indis' in request.POST:
            selected_prods = request.POST.getlist('products')
            for item in selected_prods:
                obj = Mycmd.objects.get(product=item, received = False)
                obj.indisponible = True
                obj.save()
        elif 'supp' in request.POST:
            selected_prods = request.POST.getlist('products')
            for item in selected_prods:
                obj = (Mycmd.objects.get(product=item))
                obj.deleted = True
                obj.save()
                if obj.indisponible == True and obj.deleted == True:
                    get_all_deleted_item = list(StatTable.objects.values_list('product', flat=True))
                    
                    if item not in get_all_deleted_item:
                        new_item=StatTable.objects.create(product = item)
                        new_item.cmded = 1
                        new_item.received = 0
                        new_item.indisponible = 1
                        new_item.save()
                        Mycmd.objects.get(product=item, received = False, deleted=True).delete()
                    elif item in get_all_deleted_item:
                        print(item, flush=True)
                        exiting_item = StatTable.objects.filter(product = item).update(cmded = F('cmded') + 1, indisponible = F('indisponible') + 1)
                        Mycmd.objects.get(product=item, received = False,  deleted=True).delete()
                elif obj.indisponible == False and obj.deleted == True:
                    Mycmd.objects.get(product=item).delete()


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


    return render(request,'cmd_page.html',{'current_username':current_username, 'form' : form, 'products': products, 'arts' : arts, 'My_cmd_ste' : My_cmd_ste, 'My_cmd_stf': My_cmd_stf, 'My_cmd_ord' : My_cmd_ord, 'My_cmd_q': My_cmd_q,
                    'ste_ord': ste_ord, 'stf_q' : stf_q , 'current_user'  : current_user})
   



@login_required(login_url='main-page')

def editItem(request,prod_id,*args):
    
    
    get_product = Mycmd.objects.get(pk=prod_id)
    
    form = EditItemForm(request.POST or None, instance=get_product)
    if form.is_valid():
        form.save()
        return redirect('cmd-page')
    return render(request, 'edit_item.html', {'form':form })



















