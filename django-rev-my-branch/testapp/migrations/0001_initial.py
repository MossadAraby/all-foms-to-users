# Generated by Django 4.1.7 on 2023-03-15 19:02

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
            name="Clients",
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
                (
                    "full_name",
                    models.CharField(max_length=200, verbose_name="Full Name"),
                ),
                ("address", models.CharField(max_length=200, verbose_name="Address")),
                (
                    "image",
                    models.ImageField(
                        upload_to="clients-profiles/", verbose_name="Image"
                    ),
                ),
                ("phone", models.CharField(max_length=20, verbose_name="Phone Number")),
                (
                    "join_on",
                    models.DateTimeField(auto_now_add=True, verbose_name="Join On"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="client",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Clients",
            },
        ),
    ]
