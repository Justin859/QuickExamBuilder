# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 15:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0015_auto_20171125_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='candidates',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='number_of_questions',
        ),
    ]
