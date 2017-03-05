# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 01:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No Course Title Provided', max_length=255)),
                ('info', models.CharField(default='There is no Course Description', max_length=300)),
                ('term', models.CharField(choices=[('Winter', 'Winter'), ('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall')], default='None', max_length=6)),
                ('slug', models.CharField(max_length=20, unique=True)),
                ('creator', models.CharField(default='No admin lol', max_length=255)),
                ('addCode', models.CharField(max_length=10, unique=True)),
                ('year', models.CharField(default=2017, max_length=20)),
                ('professor', models.BooleanField(default=True)),
                ('projects', models.ManyToManyField(to='projects.Project')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(through='courses.Enrollment', to=settings.AUTH_USER_MODEL),
        ),
    ]
