# Generated by Django 2.1.1 on 2018-09-23 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basecamp', '0003_auto_20180923_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='counselor',
            field=models.ForeignKey(limit_choices_to={'role': 'counselor'}, on_delete=django.db.models.deletion.CASCADE, to='basecamp.Attendee'),
        ),
        migrations.AlterField(
            model_name='activityattendee',
            name='attendee',
            field=models.ForeignKey(limit_choices_to={'role': 'camper'}, on_delete=django.db.models.deletion.CASCADE, to='basecamp.Attendee'),
        ),
    ]
