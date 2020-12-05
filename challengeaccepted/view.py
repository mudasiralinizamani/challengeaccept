from django.shortcuts import render

# Create your views here - Mudasir Ali

def Index(req):
    return render(req, 'Pages/Index.html')


def About(req):
    return render(req, 'Pages/About.html')

def Contact(req):
    return render(req, 'Pages/Contact.html')