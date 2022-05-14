from itertools import count
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView
from makecmd.models import Mycmd
from django.db.models import Sum,Count
# Create your views here.


def ProductStat(request):
    qs = Mycmd.objects.values('product').annotate(count = Count('product')).order_by('-count')[:50]
    indis_prod = Mycmd.objects.filter(indisponible = True, received = False).values('product').annotate(count2=Count('product')).order_by('-count2')[:50]
    receiv =  Mycmd.objects.values('product').annotate(count_prod = Count('product')).annotate(count_rec = Sum('received_0')).order_by('-count_rec')[:50]
    print(receiv, flush=True)
    
    
    return render (request, 'prod_stat.html',{'qs':qs,'indis_prod':indis_prod,'receiv':receiv})
