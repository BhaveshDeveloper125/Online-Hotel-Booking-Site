# Generated by Django 5.0 on 2024-03-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
