# Generated by Django 4.1.7 on 2023-12-29 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_newsletter"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(max_length=2000)),
                ("image", models.ImageField(upload_to="projects/")),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_visible", models.BooleanField(default=False)),
            ],
        ),
    ]
