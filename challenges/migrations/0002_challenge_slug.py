# Generated by Django 3.0.4 on 2020-03-27 17:45

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("challenges", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default="", editable=False, populate_from="name"
            ),
            preserve_default=False,
        ),
    ]
