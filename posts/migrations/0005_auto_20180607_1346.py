# Generated by Django 2.0.5 on 2018-06-07 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20180606_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
