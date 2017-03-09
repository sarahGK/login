from login.forms import RegistrationForm 
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *


# Create your views here.

 
@transaction.atomic
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['user_id'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            user.profile.phonenumber = form.cleaned_data['phonenumber']
            user.save()
            return HttpResponseRedirect('/login/register/success/')
    else:
        form = RegistrationForm()
 
    return render(request,'registration/register.html',{'form': form})
 
def register_success(request):
    return render(request,'registration/success.html',)
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# if a user want to access a method that that requires login and the user is not logged in 
# it will redirect the user to login page 
@login_required(login_url='/login/')
def home(request):
    return render(request,'home.html',{'user': request.user })

