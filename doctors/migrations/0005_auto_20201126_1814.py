# Generated by Django 3.1.3 on 2020-11-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_doctor_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='user_name',
            field=models.CharField(max_length=100, verbose_name='User name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=100, verbose_name='User name'),
        ),
    ]
