# Generated by Django 4.2.9 on 2024-02-19 14:31

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("farm", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Works",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now_add=True)),
                ("work_name", models.CharField(blank=True, max_length=255)),
                ("start_date_year", models.CharField(null=True)),
                ("start_date_month", models.CharField(null=True)),
                ("start_date_day", models.CharField(null=True)),
                ("end_date_year", models.CharField(null=True)),
                ("end_date_month", models.CharField(null=True)),
                ("end_date_day", models.CharField(null=True)),
                ("machine_name", models.CharField(blank=True, max_length=255)),
                ("contents", models.TextField(blank=True)),
                ("is_active", models.BooleanField(default=True)),
                ("battery", models.IntegerField(null=True)),
                ("start_point", django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ("end_point", django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ("expected_path", django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ("crop", models.CharField(null=True)),
                ("user_memo", models.TextField(blank=True)),
                ("estimated_hours", models.IntegerField(default=0, help_text="예상 작업시간: 시간")),
                ("estimated_minutes", models.IntegerField(default=0, help_text="예상 작업시간: 분")),
                (
                    "machine_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="machine_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "work_fields",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="work_farm_farmfield",
                        to="farm.farmfield",
                    ),
                ),
            ],
        ),
    ]
