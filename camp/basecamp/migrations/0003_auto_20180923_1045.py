# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-23 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basecamp', '0002_auto_20170605_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'activity',
            },
        ),
        migrations.CreateModel(
            name='ActivityAttendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='basecamp.Activity')),
            ],
            options={
                'db_table': 'activity_attendee',
            },
        ),
        migrations.AlterField(
            model_name='attendee',
            name='role',
            field=models.CharField(choices=[('counselor', 'Counselor'), ('camper', 'Camper')], max_length=32),
        ),
        migrations.AddField(
            model_name='activityattendee',
            name='attendee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basecamp.Attendee'),
        ),
        migrations.AddField(
            model_name='activity',
            name='counselor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basecamp.Attendee'),
        ),
        migrations.AlterUniqueTogether(
            name='activityattendee',
            unique_together=set([('activity', 'attendee')]),
        ),
    ]