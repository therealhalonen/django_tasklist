# Generated by Django 3.2 on 2022-05-31 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_rename_priority_job_spriority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='spriority',
            new_name='priority',
        ),
    ]
