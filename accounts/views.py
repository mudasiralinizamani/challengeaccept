from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, User


# Create your views here.

def Accounts(req):
    redirect('Signup')

def Profile(req):
    return render(req, 'Accounts/Admin.html')

def Signup(req):
    if  req.user.is_authenticated:
        messages.info(req, f'You are already Authenticated, {req.user.username}!')
        return  redirect('Index')
    else:
        form = forms.CreateUserForm()
        if req.method == 'POST':
            form = forms.CreateUserForm(req.POST)
            if form.is_valid():
                form.save()

                messages.success(req, f'Account was successfully created {form.cleaned_data.get("username")}, Now Login')
                return redirect('Index')
        
        Content = {'form': form, }
        return render(req, 'Accounts/Signup.html', Content)

def Login(req):
    if  req.user.is_authenticated:
        messages.info(req, f'You are already Login, {req.user.username}!')
        return  redirect('Index')
    else:
        if req.method == 'POST':
            username = req.POST.get('username')
            password = req.POST.get('password')

            user = authenticate(req, username=username, password=password)

            if user is not None:
                login(req, user)
                messages.success(req, f'Successfully login as, {user}')
                return redirect('Index')
            else:
                messages.error(req, 'username or passoword is incorrect')

        return render(req, 'Accounts/Login.html')

def API_Login(req):
    if  req.user.is_authenticated:
        messages.info(req, f'You are already Login, {req.user.username}!')
        return  redirect('Index')
    else:
        if req.method == 'POST':
            username = req.POST.get('username')
            password = req.POST.get('password')

            user = authenticate(req, username=username, password=password)

            if user is not None:
                login(req, user)
                messages.success(req, f'Successfully login as, {user}')
                return redirect('Index')
            else:
                messages.error(req, 'username or passoword is incorrect')
                return redirect('Index')



def Logout(req):
    logout(req)
    return redirect('Index')

