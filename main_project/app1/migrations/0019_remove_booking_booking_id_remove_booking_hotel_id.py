# Generated by Django 5.0 on 2024-03-16 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='hotel_id',
        ),
    ]
