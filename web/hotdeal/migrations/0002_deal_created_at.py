# Generated by Django 4.1.5 on 2023-01-03 05:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotdeal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]