from django.shortcuts import render
from .models import Contact as ContactModel
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

# View for Handling the Contact REQUEST - Mudsir Ali
def Contact(req):
    if req.method == 'POST':
        Name = req.POST.get('name')
        Email = req.POST.get('email')
        Message = req.POST.get('message')
        Subject = req.POST.get('subject')

        if len(Name) < 2 or len(Email) < 4 or '@' not in Email or len(Subject) <1:
            messages.error(req, 'Plz, Fill the fields Correctly.')

        else:
            contact = ContactModel(name=Name, email=Email,subject=Subject, message=Message)
            contact.save()
            send_mail(Subject, Message, Email, [settings.EMAIL_HOST_USER])
            messages.success(req, f'Thanks for Contacting, {Name}.')
    return render(req, 'Pages/Contact.html')