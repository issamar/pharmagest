from django.shortcuts import render
from .forms import ContatForm
import itertools 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='main-page')
def contact(request):
    
    form = ContatForm
    if request.method == 'POST':
        used_username = request.POST.get('user_name')
        all_users = User.objects.values_list('username')
        all_users_list = list(itertools.chain(*all_users))
        if used_username in all_users_list:
            
            form = ContatForm(request.POST)
            if form.is_valid():
                form.save()
                form= ContatForm
                messages.success(request, 'Votre message est bien transmis')
        else:
            messages.warning(request, "Cet utilisateur n'existe pas ")
    return render(request, 'contact.html', { 'form' : form})