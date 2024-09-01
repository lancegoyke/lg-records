# Generated by Django 3.0.4 on 2020-03-27 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("challenges", "0002_challenge_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="challenge",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="records",
                to="challenges.Challenge",
            ),
        ),
    ]
