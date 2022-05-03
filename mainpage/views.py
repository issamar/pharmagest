from dataclasses import fields
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from pkg_resources import require
from mainpage.models import Account, UserPayementStat
from .forms import UserForm, UserProofForm
# Create your views here.
def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('main-page')
    else: 
        form = UserForm
        if request.method =='POST':
            form = UserForm(request.POST)
            if form.is_valid():
                
                user = request.POST['username']
                form.save()
                messages.success(request,'Vous avez enregistré avec succés')
                return redirect('main-page')
    return render(request,'register.html', {'form' : form,})



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



@login_required(login_url='main-page')
def UserProofView(request):
    form = UserProofForm
    if request.method =='POST':
        
        form = UserProofForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main-page')
    return render (request, 'user_prof.html',{'form' : form})