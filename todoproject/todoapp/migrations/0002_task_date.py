# Generated by Django 3.2.8 on 2021-11-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1996-01-06'),
            preserve_default=False,
        ),
    ]
