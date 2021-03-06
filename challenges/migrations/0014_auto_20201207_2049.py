# Generated by Django 3.0.8 on 2020-12-07 20:49

import challenges.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0013_second_challenge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first_challenge',
            name='Image',
            field=models.FileField(blank=True, default='None', null=True, upload_to='Challenges/First/Users/'),
        ),
        migrations.AlterField(
            model_name='first_challenge',
            name='Video',
            field=models.FileField(blank=True, default='None', null=True, upload_to='Challenges/First/Users', validators=[challenges.validators.Check_FileSize]),
        ),
        migrations.AlterField(
            model_name='second_challenge',
            name='Image',
            field=models.FileField(blank=True, default='None', null=True, upload_to='Challenges/Second/Users/'),
        ),
        migrations.AlterField(
            model_name='second_challenge',
            name='Video',
            field=models.FileField(blank=True, default='None', null=True, upload_to='Challenges/Second/Users', validators=[challenges.validators.Check_FileSize]),
        ),
    ]
