# Generated by Django 2.2.13 on 2020-09-09 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_exercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealplanType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
    ]
