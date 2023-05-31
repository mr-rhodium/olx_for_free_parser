# Generated by Django 4.2.1 on 2023-05-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StopWord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("word", models.CharField(max_length=20, unique=True)),
            ],
            options={
                "verbose_name": "Stop word",
                "verbose_name_plural": "Stop words",
            },
        ),
    ]
