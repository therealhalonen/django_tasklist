# Generated by Django 3.2 on 2022-05-31 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20220531_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='city',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='free_field',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='priority',
            field=models.CharField(default='Urgent, Normal, Low', max_length=300),
        ),
        migrations.AddField(
            model_name='job',
            name='street_address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='supplies_needed',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
