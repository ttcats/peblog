# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 09:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170328_0742'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': '博客', 'verbose_name_plural': '博客'},
        ),
    ]
