from dataclasses import fields
from sys import flags
from tokenize import generate_tokens
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
from django.core.mail import EmailMessage
from django.views import View
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator
# Create your views here.
def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('main-page')
    else: 
        form = UserForm
        if request.method =='POST':
            form = UserForm(request.POST)
            if form.is_valid():
                user_name = request.POST['username']
                email = request.POST['email']
                all_emails = User.objects.values_list('email', flat=True)
                if email not in all_emails:
                    form.save()
                    User.objects.filter(username = user_name).update(is_active = False)
                    user_pk = User.objects.filter(username =user_name ).values_list('pk', flat=True)
                
                    user = User.objects.get(pk=user_pk[0])
                    domaine = get_current_site(request).domain
                    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                    link = reverse('activate', kwargs={'uidb64':uidb64, 'token': token_generator.make_token(user)})
                    activation_url = 'http://' + domaine+link
                    email_subject = 'Activez votre compte'
                    email_body = 'Cher(e) ' + user.username + "\n Vous avez enregistré sur le site de OffGest Pour continuer l'enregistrement veuillez cliquey sur le lien ci-dessous\n"  + activation_url
                    rec_email = 'pharmagest.22@gmail.com'
                    email = EmailMessage(
                        email_subject,
                        email_body,
                        rec_email,
                        [email],
                    )
                    email.send(fail_silently = False)  
                    messages.success(request,'Vous avez enregistré avec succés')
                    return redirect('main-page')
                else:
                    messages.warning(request,'Email deja utilisé')
        return render(request,'register.html', {'form' : form,})


class verification(View):
    def get(self,request,uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as e:
            user = None
        if user and token_generator.check_token(user,token):
            user.is_active = True
            user.save()
        return redirect('main-page')


def MainPage(request):
    userrname = request.user
    print(userrname, flush=True)
    get_userrname_id = User.objects.filter(username = userrname).values_list('id', flat=True)
    get_userrname = User.objects.get(pk=get_userrname_id[0])
    print(get_userrname.date_joined, flush=True)
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

