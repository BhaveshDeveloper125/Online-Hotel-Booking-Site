# Generated by Django 5.0 on 2024-03-12 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_hotel_request_other'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_hname', to='app1.hotels')),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_rooms', to='app1.hotels')),
            ],
        ),
    ]
