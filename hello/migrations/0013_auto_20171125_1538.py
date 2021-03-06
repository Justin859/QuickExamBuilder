# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0012_auto_20171122_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamCandidates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('exam_id', models.CharField(max_length=255)),
                ('candidate_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='candidates',
            options={'verbose_name': 'Exam Question', 'verbose_name_plural': 'Exam Questions'},
        ),
        migrations.AlterModelOptions(
            name='examquestions',
            options={},
        ),
        migrations.RenameField(
            model_name='examquestions',
            old_name='question_id',
            new_name='exam_question_id',
        ),
        migrations.RemoveField(
            model_name='examquestions',
            name='question_section',
        ),
    ]
