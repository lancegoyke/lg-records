# Generated by Django 4.1.5 on 2024-08-17 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200406_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sex',
            field=models.CharField(choices=[('U', 'Prefer not to say'), ('F', 'Female'), ('M', 'Male')], default='U', max_length=1),
        ),
    ]