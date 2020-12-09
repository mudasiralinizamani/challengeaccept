from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# This is the Form of the User Signup - Mudasir Ali
class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, help_text="Firstname")
    last_name = forms.CharField(max_length=50, help_text="Lastname")
    registration_status = forms.BooleanField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'registration_status']
