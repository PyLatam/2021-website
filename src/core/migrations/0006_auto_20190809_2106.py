# Generated by Django 2.1.9 on 2019-08-10 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190809_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conferenceregistration',
            name='is_grant_recipient',
        ),
        migrations.RemoveField(
            model_name='conferenceregistration',
            name='is_sponsor',
        ),
    ]