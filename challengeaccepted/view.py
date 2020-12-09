from main.views import Contact
from django.shortcuts import render

# Create your views here - Mudasir Ali

# Function for the Index Page
def Index(req):
    Context = {}
    if req.user.is_authenticated:
        User_Fullname = f'{req.user.first_name} {req.user.last_name}'
        User_Username = f'{req.user.username}'
        Context = {'user_fullname': User_Fullname, 'user_username': User_Username}
    else:
        Contact = {}
    return render(req, 'Pages/Index.html', Context)


# Function for the About Page
def About(req):
    return render(req, 'Pages/About.html')
