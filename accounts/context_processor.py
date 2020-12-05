from .  import forms

def API_Signup_Form(req):
    return {'api_signup_form': forms.CreateUserForm}