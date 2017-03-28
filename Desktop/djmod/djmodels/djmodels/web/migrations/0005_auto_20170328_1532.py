# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Male', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='write about title'),
        ),
    ]
