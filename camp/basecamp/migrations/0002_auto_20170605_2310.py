# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 23:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basecamp', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendee',
            unique_together=set([('camp', 'user')]),
        ),
    ]
