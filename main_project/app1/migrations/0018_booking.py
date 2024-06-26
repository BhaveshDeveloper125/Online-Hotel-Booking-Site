# Generated by Django 5.0 on 2024-03-16 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_id', models.IntegerField()),
                ('booking_id', models.IntegerField()),
                ('ariival_date', models.CharField(max_length=100)),
                ('departure_date', models.CharField(max_length=100)),
                ('booked_room_count', models.IntegerField()),
            ],
        ),
    ]
