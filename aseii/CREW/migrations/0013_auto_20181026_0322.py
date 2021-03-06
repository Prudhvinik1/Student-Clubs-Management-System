# Generated by Django 2.1.2 on 2018-10-25 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CREW', '0012_auto_20181026_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CREW.rooms'),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CREW.user'),
        ),
    ]
