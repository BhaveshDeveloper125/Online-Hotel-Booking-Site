# Generated by Django 5.0 on 2024-03-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_rename_category_hotels_category_in_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='is_luxury',
            field=models.BooleanField(default=False),
        ),
    ]