# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-04-29 15:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawHTMLPluginData',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_rawhtml_rawhtmlplugindata', serialize=False, to='cms.CMSPlugin')),
                ('body', models.TextField(verbose_name=b'HTML')),
                ('label', models.CharField(default=b'', max_length=40)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
