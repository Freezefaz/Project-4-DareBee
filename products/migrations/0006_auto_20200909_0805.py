# Generated by Django 2.2.13 on 2020-09-09 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200909_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]
