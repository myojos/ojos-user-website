# Generated by Django 3.0.7 on 2020-07-22 09:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200720_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 9, 27, 52, 627199, tzinfo=utc)),
        ),
    ]
