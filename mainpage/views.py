from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def MainPage(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        pass_word = request.POST['password']
        user = authenticate(request, username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return redirect('cmd-page')
        else:
            messages.warning(request, 'informations erronées reéssayer')
            return redirect('main-page')
        

        
    return render(request, 'index.html',{})
def logout_user(request):
    logout(request)
    return redirect('main-page')