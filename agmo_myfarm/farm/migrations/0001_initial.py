# Generated by Django 4.2.9 on 2024-02-12 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FarmField",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("field_name", models.CharField(blank=True, max_length=255)),
                ("location", models.JSONField(null=True)),
                ("crop", models.JSONField(null=True)),
                ("weather_date", models.CharField(null=True)),
                ("weather_time", models.CharField(null=True)),
                ("is_rain", models.FloatField(null=True)),
                ("rain_sh", models.CharField(null=True)),
                ("temperature", models.FloatField(null=True)),
                ("humidity", models.FloatField(null=True)),
                ("wind_direction", models.CharField(null=True)),
                ("wind_speed", models.FloatField(null=True)),
                ("sky_sh", models.CharField(null=True)),
                ("user_memo", models.TextField(blank=True, null=True)),
                ("is_selected", models.BooleanField(default=False)),
                (
                    "farm_field_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="field_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
