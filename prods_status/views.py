
from itertools import count, product
import itertools 
from multiprocessing import context
from operator import methodcaller
from unittest import result
from django.contrib.auth.decorators import login_required
from makecmd.decoators import Time_to_pay
import re
from django.shortcuts import render
from django.views.generic import TemplateView
from makecmd.models import Mycmd,StatTable
from django.db.models import Sum,Count
from addmed.models import Addmed
import json
# Create your views here.

@login_required(login_url='main-page')
@Time_to_pay
def ProductStat(request):
    qs = StatTable.objects.values('product').annotate(count = Count('product')).annotate(count_cmd = Sum('cmded')).order_by('-count_cmd')[:50]
    indis_prod = StatTable.objects.filter(indisponible__gt=0).values('product').annotate(count2=Sum('indisponible')).order_by('-count2')[:50]
    receiv =  StatTable.objects.values('product').annotate(count_prod = Count('product')).annotate(count_cmd=Sum('cmded')).annotate(count_rec = Sum('received')).annotate(count_indis = Sum('indisponible')).order_by('-count_cmd')[:50]
    products = StatTable.objects.all().order_by('product')
    
    if request.method == 'POST':
        get_checked = request.POST.getlist('products')
        items_list=[]
        for item in get_checked:
            
            get_db_items = StatTable.objects.get(product=item)
            items_list.append(get_db_items)
        
        return render (request, 'prod_stat.html',{'qs':qs,'indis_prod':indis_prod,'receiv':receiv, 'products':products,'items_list':items_list })

            


 

        
    return render (request, 'prod_stat.html',{'qs':qs,'indis_prod':indis_prod,'receiv':receiv, 'products':products })
