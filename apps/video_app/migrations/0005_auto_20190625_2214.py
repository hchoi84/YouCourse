# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-25 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
        ('video_app', '0004_auto_20190625_0234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='likes',
        ),
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(related_name='videos_liked', to='user_app.User'),
        ),
    ]
