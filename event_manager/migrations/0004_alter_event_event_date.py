# Generated by Django 4.0.4 on 2022-05-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_manager', '0003_event_event_status_alter_event_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(),
        ),
    ]