from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Registered_Users(models.Model):

    User_full_name = models.CharField(max_length=60)
    User_username  = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.User_full_name} {self.User_username}'



class UserOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    otp = models.SmallIntegerField()

