# Generated by Django 5.0.6 on 2024-06-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0005_remove_cardioexercise_is_aerobic_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="is_rest",
            field=models.BooleanField(default=False),
        ),
    ]
