"""challengeaccepted URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import view
from django.conf import settings
from django.conf.urls.static import static
from main.views import Contact


admin.site.site_header = "Challenge Accept Admin"
admin.site.site_title = "Challenge Accept Admin Panel"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.Index, name='Index'),
    path('about/', view.About, name='About'),
    
    path('contact/', Contact, name='Contact'),


    path('accounts/', include('accounts.urls')),
    path('challenges/', include('challenges.urls'))


]

# This is for the Media Files, Without this Media Files will be served - Mudasir Ali
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)