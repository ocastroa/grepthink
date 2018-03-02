# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-28 21:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=200)),
                ('slug', models.CharField(max_length=20, null=True, unique=True)),
                ('members', models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Scrum Boards',
                'verbose_name_plural': 'Scrum Boards',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=200)),
                ('slug', models.CharField(default='', max_length=20, null=True, unique=True)),
                ('board', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='column_board', to='scrumboard.Board')),
            ],
            options={
                'verbose_name': 'Column',
                'verbose_name_plural': 'Column',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned', models.BooleanField(default=False)),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=400)),
                ('slug', models.CharField(default='', max_length=20, null=True, unique=True)),
                ('board', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='task_board', to='scrumboard.Board')),
                ('column', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='column', to='scrumboard.Column')),
                ('userID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Task',
            },
        ),
    ]
