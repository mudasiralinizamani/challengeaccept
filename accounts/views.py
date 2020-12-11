import django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth.models import User as User_Model_D
from .models import Registered_Users, UserOTP
from random import randint
from django.core.mail import EmailMessage, message
from django.conf import settings




# Create your views here.

Users_are_Registered = Registered_Users.objects.all()

Registered_Users_List = []

Users = User_Model_D.objects.all()
All_Users = []


for User in Users:
    All_Users.append(str(User.username))


for User in Users_are_Registered:
    Registered_Users_List.append(str(User))


def Accounts(req):
    redirect('Signup')

def Profile(req):
    return render(req, 'Accounts/Admin.html')

# Function to Create a User Account - Mudasir Ali
def Signup(req):
    if  req.user.is_authenticated:
        messages.info(req, f'You are already Authenticated, {req.user.username}!')
        return  redirect('Index')

    else:
        form = forms.CreateUserForm()

        if req.method == 'POST':
            # Getting all the Fields from the Signup Form - Mudasir Ali
            get_otp = req.POST.get('otp')
            Username = req.POST.get('username')
            Firstname = req.POST.get('fname')
            Lastname = req.POST.get('lname')
            Email = req.POST.get('email')
            Password = req.POST.get('password')
            Passwordc = req.POST.get('passwordc')

            # Checking the OTP is insert - Mudasir Ali
            if get_otp:
                get_usr = req.POST.get('usr')
                usr = User_Model_D.objects.get(username=get_usr)

                # Checking the OTP Verification  - Mudasir Ali
                if int(get_otp) == UserOTP.objects.filter(user=usr).last().otp:
                    messages.success(req, f'Account is Successfully created {usr.username}')
                    usr.is_active = True
                    usr.save()
                    return redirect('Login')
                else:
                    messages.error(req, f'Sorry, Plz enter the valid OTP.')
                    return render(req, 'Accounts/Signup.html', {'otp': True, 'user': usr})

            # If the OTP is not insert then the Signup will Rendered - Mudair Ali
            else:
                
                # Saving that User typed in the Form - Mudasir Ali
                typed_username = str(Username)
                typed_firstname = str(Firstname)
                typed_lastname = str(Lastname)
                typed_email = str(Email)

                Content = {'typed_username': typed_username, 'typed_firstaname': typed_firstname, 'typed_lastname': typed_lastname, 'typed_email': typed_email}

                # Checks For Errors - Mudasir Ali

                if Username in All_Users:
                    messages.error(req, f'username: {Username}, already exists in database')
                    return render(req, 'Accounts/Signup.html', Content)

                if '@gmail.com' not in Email:
                    messages.error(req, f'Invalid Email')
                    return render(req, 'Accounts/Signup.html', Content)

                if Password != Passwordc:
                    messages.error(req, f'Password is not matching to the Confirm Password')
                    return render(req, 'Accounts/Signup.html', Content)

                # Creating the USER in_active, So the User cannot login, 
                # After the OTP verification the USER wil active - Mudasir ALi

                myuser = User_Model_D.objects.create_user(Username, Email, Passwordc)
                myuser.first_name = Firstname
                myuser.last_name = Lastname
                myuser.is_active = False
                myuser.save()

                # Creating the OTP for the USER - Mudasir Ali
                user_otp = randint(100000, 999999)

                # Saving OTP in the Database - Mudasir Ali
                User_OTP_Model = UserOTP(user=myuser, otp=user_otp)
                User_OTP_Model.save()

                # Sending Email to the USER GMAIL, and this email user will get OTP - Mudasir Ali
                email = EmailMessage('Challenge Accept - Verify OTP', f'Hi {Username}, Your OTP is {user_otp}', settings.EMAIL_HOST_USER, [Email])
                email.send()

                messages.info(req, f'An OTP has been sent to your Gmail. Enter the OTP')                    
                return render(req, 'Accounts/Signup.html', {'otp': True, 'user': myuser})

        Content = {'form': form, }
        return render(req, 'Accounts/Signup.html', Content)



# Function to Login a User
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


# API Function to Login User, This function can be accessed from anywhere,
# but this function will take Two Fields USERNAME and PASSWORD - Mudasir Ali
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


# This Function will logout User, If the user is already login  - Mudasir Ali
def Logout(req):
    if req.user.is_authenticated:    
        logout(req)
        messages.success(req, 'Now you are Logout')
        return redirect('Index')
    else:
        messages.info('You are not Login')
        return redirect('Index')
