# Generated by Django 4.2.9 on 2024-02-09 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("farm", "0002_remove_machine_farm_machine_user_delete_weather_and_more"),
        ("work", "0002_remove_works_end_date_remove_works_start_date_and_more"),
        ("home", "0002_remove_home_home_machines_remove_home_home_weather"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Machine",
        ),
    ]
