# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170328_0651'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AlterModelOptions(
            name='blogtag',
            options={'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='tag',
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(to='blog.BlogTag'),
        ),
    ]
