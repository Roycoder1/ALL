# Generated by Django 4.1 on 2022-08-18 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Visitor",
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
                ("images", models.URLField()),
                ("description", models.TextField()),
                ("area", models.TextField()),
            ],
        ),
    ]
