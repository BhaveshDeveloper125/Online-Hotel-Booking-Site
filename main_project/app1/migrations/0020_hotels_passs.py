# Generated by Django 5.0 on 2024-03-16 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_remove_booking_booking_id_remove_booking_hotel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='passs',
            field=models.CharField(default=123456, max_length=25),
        ),
    ]
