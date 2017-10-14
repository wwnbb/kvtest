# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 05:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20171013_1249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['text']},
        ),
        migrations.AddField(
            model_name='link',
            name='named_url',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='link',
            name='path',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='link',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='menu.Link'),
        ),
    ]
