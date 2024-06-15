# Generated by Django 5.0 on 2024-03-22 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_hotel_request_password1_hotel_request_password2'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='price_per_room',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
