# Generated by Django 5.0 on 2024-02-19 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("algorithms", "0005_alter_algorithm_algorithm_file"),
        ("endpoints", "0002_endpoint_algorithm"),
    ]

    operations = [
        migrations.AddField(
            model_name="endpoint",
            name="status",
            field=models.CharField(
                choices=[
                    ("creating", "creating"),
                    ("active", "active"),
                    ("terminating", "terminating"),
                ],
                default="creating",
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="endpoint",
            name="algorithm",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="algorithms.algorithm",
            ),
        ),
    ]
