# Generated by Django 3.0.8 on 2020-12-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registered_Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_full_name', models.CharField(max_length=60)),
                ('User_username', models.CharField(max_length=70)),
            ],
        ),
    ]
