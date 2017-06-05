# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 21:36
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
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[(b'counselor', b'Counselor'), (b'camper', b'Camper')], max_length=32)),
            ],
            options={
                'db_table': 'attendee',
            },
        ),
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'camp',
            },
        ),
        migrations.AddField(
            model_name='attendee',
            name='camp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basecamp.Camp'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
