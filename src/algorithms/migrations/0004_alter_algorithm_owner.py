# Generated by Django 4.2.8 on 2023-12-06 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("algorithms", "0003_alter_algorithm_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="algorithm",
            name="owner",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
