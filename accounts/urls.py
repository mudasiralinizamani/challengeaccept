from django.urls import path
from . import views

# Create the Accounts Urls - Mudasir ALi

urlpatterns = [
    path('', views.Accounts, name="Accounts"),
   path('signup/', views.Signup, name="Signup"),
   path('login/', views.Login, name="Login"),
   path('logout/', views.Logout, name="Logout"),
   path('profile/', views.Profile, name="Profile"),

    # API Login Url
   path('api-login/', views.API_Login, name='API_Login'),
]