# Generated by Django 5.0.6 on 2024-06-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1994-05-23'),
            preserve_default=False,
        ),
    ]