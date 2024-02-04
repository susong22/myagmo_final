# Generated by Django 4.2.9 on 2024-02-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_email_alter_user_password_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name="User name"),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(blank=True, max_length=255, unique=True, verbose_name="Phone Number"),
        ),
    ]
