# Generated by Django 4.2.9 on 2024-02-20 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("farm", "0004_farmfield_one_after_sky_sh_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="farmfield",
            name="location_list",
            field=models.JSONField(null=True),
        ),
    ]
