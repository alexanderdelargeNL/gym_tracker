# Generated by Django 5.0.6 on 2024-06-17 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0003_rename_exercise_subject"),
    ]

    operations = [
        migrations.CreateModel(
            name="CardioExercise",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("is_aerobic", models.BooleanField(default=True)),
            ],
        ),
        migrations.RenameModel(
            old_name="Subject",
            new_name="MuscleGroup",
        ),
        migrations.RenameField(
            model_name="activity",
            old_name="type",
            new_name="musclegroup",
        ),
        migrations.AddField(
            model_name="activity",
            name="cardioexercise",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="activities.cardioexercise",
            ),
        ),
    ]