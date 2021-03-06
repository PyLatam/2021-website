# Generated by Django 2.1.11 on 2019-08-26 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(limit_choices_to={'registration__isnull': False}, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='account.Account')),
            ],
        ),
        migrations.AddField(
            model_name='lead',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='leads.LeadGroup'),
        ),
    ]
