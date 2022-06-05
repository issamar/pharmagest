
from itertools import count, product
import itertools
from math import lgamma 
from multiprocessing import context

from django.contrib.auth.decorators import login_required
from makecmd.decoators import Time_to_pay
import re
from django.shortcuts import render

from makecmd.models import Mycmd,StatTable
from django.db.models import Sum,Count


# Create your views here.

@login_required(login_url='main-page')
@Time_to_pay
def ProductStat(request):
    qs = StatTable.objects.filter(product__startswith='M:').annotate(count = Count('product')).annotate(count_cmd = Sum('cmded')).order_by('-count_cmd')[:50]
    indis_prod = StatTable.objects.filter(indisponible__gt=0).filter(product__startswith='M:').values('product').annotate(count2=Sum('indisponible')).order_by('-count2')[:50]
    receiv =  StatTable.objects.filter(product__startswith='M:').annotate(count_prod = Count('product')).annotate(count_cmd=Sum('cmded')).annotate(count_rec = Sum('received')).annotate(count_indis = Sum('indisponible')).order_by('-count_cmd')[:50]
    products = StatTable.objects.filter(product__startswith='M:').values().order_by('product')
    real_stat = Mycmd.objects.filter(product__startswith='M').values('product').annotate(count_prod=Count('product')).order_by('-count_prod')[:50]
    

    if request.method == 'POST':
        get_checked = request.POST.getlist('products')
        items_list=[]
        for item in get_checked:
            
            get_db_items = StatTable.objects.get(product=item)
            items_list.append(get_db_items)
        
        return render (request, 'prod_stat.html',{'qs':qs,'indis_prod':indis_prod,'receiv':receiv, 'products':products,'items_list':items_list })

            


 

        
    return render (request, 'prod_stat.html',{'qs':qs,'indis_prod':indis_prod,'receiv':receiv, 'products':products ,'real_stat':real_stat})
