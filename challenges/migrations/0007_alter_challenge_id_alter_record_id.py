# Generated by Django 4.1.5 on 2024-08-17 03:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("challenges", "0006_auto_20200331_1902"),
    ]

    operations = [
        migrations.AlterField(
            model_name="challenge",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="record",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
