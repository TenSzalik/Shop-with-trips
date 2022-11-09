# Generated by Django 4.1.3 on 2022-11-05 23:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("planet", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="planet",
            name="price",
        ),
        migrations.AddField(
            model_name="planet",
            name="fun_fact",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="planet",
            name="surface_temperature",
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.CreateModel(
            name="Trip",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_modified", models.DateTimeField(auto_now=True)),
                ("note", models.TextField(blank=True)),
                ("price", models.FloatField()),
                ("date_start", models.DateTimeField()),
                ("date_end", models.DateTimeField()),
                ("is_safely", models.BooleanField(default=False)),
                ("description", models.TextField()),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="%(app_label)s_%(class)s_related",
                        related_query_name="%(app_label)s_%(class)ss",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "planet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="planet.planet"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]