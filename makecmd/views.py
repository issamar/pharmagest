from django.shortcuts import render
from addmed.models import Addmed
# Create your views here.
def CmdPage(request):
    products = Addmed.objects.all()
    print(products[0], flush=True)
    return render(request,'cmd_page.html',{'products': products})