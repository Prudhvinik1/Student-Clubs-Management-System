# Generated by Django 2.1.2 on 2018-10-29 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CREW', '0024_auto_20181028_2113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='poll_content',
            new_name='poll_description',
        ),
    ]
