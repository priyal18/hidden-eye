# Generated by Django 2.2 on 2020-09-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realsecurity', '0002_auto_20200905_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]