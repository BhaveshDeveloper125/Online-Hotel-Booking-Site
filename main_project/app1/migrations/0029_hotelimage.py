# Generated by Django 5.0 on 2024-04-16 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_remove_hotel_request_password1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='documents/%Y/%m/%d/')),
                ('hotel', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='hotel_images', to='app1.hotel_request')),
            ],
        ),
    ]
