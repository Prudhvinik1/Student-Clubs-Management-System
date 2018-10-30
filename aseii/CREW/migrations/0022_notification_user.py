# Generated by Django 2.1.2 on 2018-10-28 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CREW', '0021_auto_20181028_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_type', models.BooleanField(default=False)),
                ('notification_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CREW.notification')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CREW.user')),
            ],
        ),
    ]