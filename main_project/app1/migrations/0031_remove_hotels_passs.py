# Generated by Django 5.0 on 2024-04-17 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0030_remove_hotel_request_other'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='passs',
        ),
    ]
