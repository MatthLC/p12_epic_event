# Generated by Django 4.0.4 on 2022-05-23 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_manager', '0006_remove_event_contract'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='contributors',
        ),
        migrations.DeleteModel(
            name='EventContributor',
        ),
    ]
