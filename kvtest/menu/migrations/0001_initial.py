# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 04:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Menu'),
        ),
        migrations.AddField(
            model_name='item',
            name='parent_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Item'),
        ),
    ]