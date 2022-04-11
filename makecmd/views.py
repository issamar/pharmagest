from itertools import product
from django.shortcuts import render
from addmed.models import Addmed, Addart
from .models import Mycmd
from .forms import MycmdForm
# Create your views here.
def CmdPage(request):
    meds = Mycmd.objects.values_list('product')
    
    print(meds, flush=True)
    for med in meds:
        meds_list = list(med)
        print(meds_list, flush=True)
    
    products = Addmed.objects.all()
        #pull all arts from db
    arts = Addart.objects.all()

    print(arts, flush=True)
  

    if request.method == 'POST':
        
        form = MycmdForm(request.POST)
        
        if form.is_valid():
            
            form.save()

       
    return render(request,'cmd_page.html',{'products': products, 'arts' : arts})























