# Generated by Django 3.2 on 2022-05-31 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_auto_20220531_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='supplies_needed',
            field=models.CharField(choices=[('All', 'ALL'), ('Lockpick Kit', 'LOCKPICK KIT'), ('DRILL', 'DRILL'), ('Casual', 'CASUAL'), ('Non Specific', 'NON SPECIFIC')], default='All', max_length=300),
        ),
    ]