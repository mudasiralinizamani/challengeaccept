from django.core.exceptions import ValidationError


# Validator Function for Checking the File Which a User will upload in Challenges -Mudasir Ali
def Check_FileSize(value):
    filesize = value.size

    if filesize > 500000000:
        raise ValidationError('Sorry, The file must be under 60 MB')
