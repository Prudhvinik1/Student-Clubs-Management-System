# Generated by Django 2.1.2 on 2018-10-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CREW', '0020_auto_20181028_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_media',
            name='event_media',
        ),
        migrations.RemoveField(
            model_name='event_media',
            name='event_media_id',
        ),
        migrations.AddField(
            model_name='event_media',
            name='media',
            field=models.FileField(blank=True, upload_to='event_media'),
        ),
    ]
