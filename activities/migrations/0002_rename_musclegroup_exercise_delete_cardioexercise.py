# Generated by Django 5.0.6 on 2024-06-17 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MuscleGroup",
            new_name="Exercise",
        ),
        migrations.DeleteModel(
            name="CardioExercise",
        ),
    ]
