# Generated by Django 3.1.3 on 2020-11-26 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_auto_20201126_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='user_name',
        ),
    ]
