# Generated by Django 4.2.1 on 2023-05-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_attendee_events_alter_event_attendees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=100, verbose_name='Description'),
        ),
    ]