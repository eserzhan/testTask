# Generated by Django 4.1.5 on 2023-01-22 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_date_of_birth_alter_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2023, 1, 22, 8, 18, 41, 479087)),
        ),
    ]
