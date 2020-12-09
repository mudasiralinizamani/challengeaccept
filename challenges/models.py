from django.db import models
from django.contrib.auth.models import User
from .validators import Check_FileSize

# Create your models here.

import os

# This function was created for crate dynamic upload_to paths, But this is not in use - Mudasir Ali
def get_upload_path(instance, filename):
    return os.path.join(
      "user_%d" % instance.User_username.id, "car_%s" % instance.slug, filename)

# Model of the First Challenge - Mudasir Ali
class First_Challenge(models.Model):
    User_full_name = models.CharField(max_length=60)
    User_username  = models.CharField(max_length=70)

    Image = models.FileField(upload_to=f'Challenges/First/Users/', default='None', null=True, blank=True)

    Video = models.FileField(upload_to=f'Challenges/First/Users', default='None', null=True, blank=True, validators=[Check_FileSize])

    def __str__(self):
        return f'{self.User_full_name}'


# Model for the Second Challenge
class Second_Challenge(models.Model):
    User_full_name = models.CharField(max_length=60)
    User_username  = models.CharField(max_length=70)

    Image = models.FileField(upload_to=f'Challenges/Second/Users/', default='None', null=True, blank=True)

    Video = models.FileField(upload_to=f'Challenges/Second/Users', default='None', null=True, blank=True, validators=[Check_FileSize])

    def __str__(self):
        return f'{self.User_full_name}'

