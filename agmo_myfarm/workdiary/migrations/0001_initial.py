# Generated by Django 4.2.9 on 2024-02-19 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("work", "0001_initial"),
        ("tracking", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkDiary",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now_add=True)),
                ("selected_date", models.DateField()),
                ("mymemo", models.TextField(blank=True)),
                (
                    "workdiary_progress",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workdiary_tracking_progress",
                        to="tracking.progress",
                    ),
                ),
                (
                    "workdiary_tracking",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workdiary_tracking_tracking",
                        to="tracking.tracking",
                    ),
                ),
                (
                    "workdiary_work_detail",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workdiary_work_workdetail",
                        to="work.works",
                    ),
                ),
            ],
        ),
    ]
