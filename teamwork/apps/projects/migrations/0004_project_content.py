# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_project_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='content',
            field=models.TextField(default='Content', max_length=4000),
        ),
    ]