# Generated by Django 2.1.2 on 2018-10-28 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CREW', '0014_post_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_file',
        ),
        migrations.AlterField(
            model_name='club',
            name='club_tc',
            field=models.FileField(upload_to='club_t&c'),
        ),
        migrations.AlterField(
            model_name='post_media',
            name='media',
            field=models.FileField(blank=True, upload_to='post_media'),
        ),
    ]
