from django.contrib import messages
from django.shortcuts import render, redirect
from .models import First_Challenge, Second_Challenge
from accounts.views import Registered_Users_List

# Create your views here.

Challenges_1 = First_Challenge.objects.all()
Challenges_2 = Second_Challenge.objects.all()

# Dict for Contain all the Users. The Participated in Challenges
First_Challenge_Users = []
Second_Challenge_Users = []


for Challenge in Challenges_1:
    First_Challenge_Users.append(str(Challenge))

for Challenge in Challenges_2:
    Second_Challenge_Users.append(str(Challenge))



def Challenges(req):
    return redirect('Challenges_First')



# View Function for First Challenge - Mudasir Ali
def Challenges_First(req):
    # Checking the USer is Authenticated - Mudasir Ali
    if req.user.is_authenticated:
        if req.method == 'POST':
            Image = req.FILES.get('Image')
            Video = req.FILES.get('Video')

            Fullname = str(f'{req.user.first_name} {req.user.last_name}')
            Username = str(req.user.username)
            
 
            if Fullname in Registered_Users_List:
    
                Model = First_Challenge(User_full_name=Fullname, User_username=Username, Image=Image, Video=Video)
                Model.save()

                messages.success(req, f'{req.user.first_name}, You files are Successfully Uploaded.')

                return redirect('Index')
            else:
                messages.info(req, f'Sorry {Fullname}, You have to register to upload.')
                return redirect('Index')
        return render(req, 'Challenges/First.html')

    # And if the user is not Authenticated It will be redirected to the Login Page - Mudasir Ali
    else:
        messages.error(req, 'Sorry, You are not authenticated')
        return redirect('Login')



# View Functions for Second Challenge - Mudasir Ali
def Challenges_Second(req):
    # Checking the USer is Authenticated - Mudasir Ali
    if req.user.is_authenticated:
        if req.method == 'POST':
            Image = req.FILES.get('Image')
            Video = req.FILES.get('Video')

            Fullname = str(f'{req.user.first_name} {req.user.last_name}')
            Username = str(req.user.username)

            if Fullname in Registered_Users_List:
                    
                Model = Second_Challenge(User_full_name=Fullname, User_username=Username, Image=Image, Video=Video)
                Model.save()

                messages.success(req, f'{req.user.first_name}, You files are Successfully Uploaded.')

                return redirect('Index')
            else:
                messages.info(req, f'Sorry {Fullname}, You have to register to upload.')
                return redirect('Index')
        return render(req, 'Challenges/Second.html')

    # And if the user is not Authenticated It will be redirected to the Login Page - Mudasir Ali
    else:
        messages.error(req, 'Sorry, You are not authenticated')
        return redirect('Login')