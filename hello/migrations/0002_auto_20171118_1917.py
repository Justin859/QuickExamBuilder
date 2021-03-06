# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=1001)),
                ('question_id', models.CharField(max_length=1001)),
                ('answer_field_1', models.BooleanField(default=False)),
                ('answer_field_2', models.BooleanField(default=False)),
                ('answer_field_3', models.BooleanField(default=False)),
                ('answer_field_4', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=255)),
                ('question_text', models.TextField(max_length=500)),
                ('question_type', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=1001)),
                ('marks', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='greeting',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]
