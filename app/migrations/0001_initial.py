# Generated by Django 3.0.7 on 2020-07-19 10:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=20)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2020, 7, 19, 10, 7, 45, 400229, tzinfo=utc))),
                ('location', models.CharField(max_length=20)),
                ('auth_key', models.CharField(max_length=20)),
                ('auth_pass', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(verbose_name='Timestamp')),
                ('video_link', models.CharField(max_length=300)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Camera')),
            ],
        ),
    ]
