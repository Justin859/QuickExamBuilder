# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 17:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20171118_1917'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MultipleChoice',
        ),
    ]