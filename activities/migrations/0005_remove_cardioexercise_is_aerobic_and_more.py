# Generated by Django 5.0.6 on 2024-06-17 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0004_cardioexercise_rename_subject_musclegroup_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cardioexercise",
            name="is_aerobic",
        ),
        migrations.RemoveField(
            model_name="musclegroup",
            name="is_aerobic",
        ),
    ]