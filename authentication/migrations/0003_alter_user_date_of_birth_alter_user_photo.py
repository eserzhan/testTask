# Generated by Django 4.1.5 on 2023-01-20 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_date_of_birth_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2023, 1, 20, 11, 27, 31, 329232)),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
