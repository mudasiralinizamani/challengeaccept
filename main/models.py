from django.db import models

# Create your models here.


# Model for Save user Contact Info - Mudasir Ali
class Contact(models.Model):
    Person_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    subject = models.CharField(max_length=100, default='')
    message = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name