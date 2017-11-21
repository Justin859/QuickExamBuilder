# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_delete_multiplechoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=1001)),
                ('question_id', models.CharField(max_length=1001)),
                ('answer_field_1', models.CharField(max_length=255)),
                ('answer_field_2', models.CharField(max_length=255)),
                ('answer_field_3', models.CharField(max_length=255)),
                ('answer_field_4', models.CharField(max_length=255)),
                ('correct_answer', models.CharField(max_length=255)),
            ],
        ),
    ]
