# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_course_professor'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.BooleanField(default=True),
        ),
    ]
