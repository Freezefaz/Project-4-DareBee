# Generated by Django 2.2.13 on 2020-09-25 08:22

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_exercise_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealplan',
            name='cover',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
