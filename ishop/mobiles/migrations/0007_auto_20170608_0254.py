# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-08 02:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0006_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='products',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
