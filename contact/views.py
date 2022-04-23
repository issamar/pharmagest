from django.shortcuts import render
from .forms import ContatForm
from django.contrib import messages
# Create your views here.
def contact(request):
    current_username = request.user
    form = ContatForm
    if request.method == 'POST':
        form = ContatForm(request.POST)
        if form.is_valid():
            form.save()
            form= ContatForm
            messages.success(request, 'Votre message est bien transmis')
    return render(request, 'contact.html', { 'current_username' : current_username,'form' : form})