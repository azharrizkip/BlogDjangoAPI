# Generated by Django 2.0.5 on 2018-05-28 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20180528_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.Posts'),
        ),
    ]
