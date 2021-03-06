# Generated by Django 2.1.2 on 2018-10-28 14:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CREW', '0018_auto_20181028_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='club_startdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 28, 14, 9, 23, 289103, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='club_admin',
            name='date_of_joining',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 28, 14, 9, 23, 291250, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='club_registered_member',
            name='date_of_joining',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 28, 14, 9, 23, 292097, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 28, 14, 9, 23, 299114, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 28, 14, 9, 23, 295125, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 28, 14, 9, 23, 295125, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event_registered_user',
            name='register_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 28, 14, 9, 23, 300109, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leave_club_log',
            name='date_of_leaving',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 28, 14, 9, 23, 308057, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='login',
            name='datetime_of_login',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 28, 14, 9, 23, 305060, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='logout_log',
            name='logout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 28, 14, 9, 23, 309086, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 28, 14, 9, 23, 296120, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='poll',
            name='end_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 28, 14, 9, 23, 301107, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='poll',
            name='start_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 28, 14, 9, 23, 301107, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 28, 14, 9, 23, 297120, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='remove_club_log',
            name='remove_datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 28, 14, 9, 23, 309086, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 28, 14, 9, 23, 293129, tzinfo=utc)),
        ),
    ]
