# Generated by Django 4.2.9 on 2024-02-21 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("work", "0003_remove_works_solution_on"),
    ]

    operations = [
        migrations.AddField(
            model_name="works",
            name="turn_over",
            field=models.BooleanField(default=False),
        ),
    ]
