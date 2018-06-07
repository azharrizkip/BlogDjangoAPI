# Generated by Django 2.0.5 on 2018-06-06 08:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_posts_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='posts',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]