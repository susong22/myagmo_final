# Generated by Django 4.2.9 on 2024-02-20 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workdiary", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="workdiary",
            name="is_complete",
            field=models.BooleanField(default=False),
        ),
    ]
