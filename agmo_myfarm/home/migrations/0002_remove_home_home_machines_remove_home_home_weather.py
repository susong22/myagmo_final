# Generated by Django 4.2.9 on 2024-02-09 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="home",
            name="home_machines",
        ),
        migrations.RemoveField(
            model_name="home",
            name="home_weather",
        ),
    ]
