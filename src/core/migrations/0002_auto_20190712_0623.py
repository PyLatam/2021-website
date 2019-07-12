# Generated by Django 2.1.9 on 2019-07-12 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferenceregistration',
            name='is_grant_recipient',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='conferenceregistration',
            name='is_sponsor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='conferenceregistration',
            name='reservation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='registrations', to='core.Reservation'),
        ),
    ]
