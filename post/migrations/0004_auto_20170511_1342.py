# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20170511_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Article',
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
    ]