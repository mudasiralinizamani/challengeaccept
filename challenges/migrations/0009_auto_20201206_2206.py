# Generated by Django 3.0.8 on 2020-12-06 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0008_auto_20201206_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first_challenge',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='Challenges/First/Users/<django.db.models.fields.CharField><django.db.models.fields.CharField>/'),
        ),
        migrations.AlterField(
            model_name='first_challenge',
            name='Video',
            field=models.FileField(blank=True, null=True, upload_to='Challenges/First/Users/<django.db.models.fields.CharField><django.db.models.fields.CharField>/'),
        ),
    ]