from django import forms
from .models import First_Challenge, Second_Challenge


# For for the First Challenge - Mudasir Ali
class First_Challenge_Form(forms.ModelForm):
    class Meta:
        model = First_Challenge
        fields = ('Image', 'Video')


# Form for the Second Challenge - Mudasir Ali
class Second_Challenge_Form(forms.ModelForm):
    class Meta:
        model = Second_Challenge
        fields = ('Image', 'Video')