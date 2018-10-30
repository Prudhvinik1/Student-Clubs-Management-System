# Generated by Django 2.1.2 on 2018-10-25 18:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CREW', '0007_auto_20181025_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='event_media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_media_id', models.IntegerField(default=1)),
                ('media_type', models.CharField(max_length=30)),
                ('event_media', models.FileField(upload_to='')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CREW.event')),
            ],
        ),
        migrations.CreateModel(
            name='leave_club_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_club_id', models.IntegerField(default=1)),
                ('date_of_leaving', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('reason', models.TextField()),
                ('club_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CREW.club')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CREW.user')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_id', models.IntegerField(default=1)),
                ('datetime_of_login', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CREW.user')),
            ],
        ),
        migrations.CreateModel(
            name='media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(upload_to='')),
                ('media_type', models.CharField(max_length=30)),
                ('club_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CREW.club')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CREW.user')),
            ],
        ),
        migrations.CreateModel(
            name='poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_title', models.CharField(max_length=50)),
                ('poll_content', models.TextField()),
                ('poll_winner', models.IntegerField(default=1)),
                ('start_datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('end_datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CREW.user')),
            ],
        ),
        migrations.CreateModel(
            name='poll_options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=30)),
                ('poll_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CREW.poll')),
            ],
        ),
        migrations.CreateModel(
            name='poll_participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CREW.poll_options')),
                ('poll_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CREW.poll')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CREW.user')),
            ],
        ),
    ]