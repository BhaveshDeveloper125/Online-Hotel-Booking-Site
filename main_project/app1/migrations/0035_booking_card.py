# Generated by Django 5.0 on 2024-04-19 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0034_hotels_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='card',
            field=models.CharField(default='no_card', max_length=50),
        ),
    ]