# Generated by Django 5.0.1 on 2024-02-15 18:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("client_order", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientorder",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
