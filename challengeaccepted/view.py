from django.shortcuts import render

# Create your views here - Mudasir Ali

def Index(req):
    return render(req, 'Pages/Index.html')
