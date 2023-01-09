from django.shortcuts import render
from cloture.models import Closure
from django.db.models import Sum, Avg, Min, Max, Count
from datetime import datetime
# Create your views here.
def dashboard(request):
    
    #current_month = datetime.now().month
    #print(current_month, flush=True)
    #month_money = Closure.objects.filter(creation_date = current_month).aggregate(Entry = Sum('closure_paper'))
    #print(month_money, flush=True)
    return render (request, 'main-dash.html',{})