# Generated by Django 2.0.5 on 2018-05-28 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='posts',
            new_name='post',
        ),
    ]
