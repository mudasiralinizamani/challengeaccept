from django.urls import path
from . import views

# Create the Accounts Urls - Mudasir ALi

urlpatterns = [
    path('', views.Challenges, name='Challenges'),
    path('first/', views.Challenges_First, name='Challenges_First'),
    path('second/', views.Challenges_Second, name='Challenges_Second')
]