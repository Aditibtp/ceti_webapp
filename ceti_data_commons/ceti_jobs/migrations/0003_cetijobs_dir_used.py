# Generated by Django 2.2.5 on 2019-11-11 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ceti_jobs', '0002_auto_20191110_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='cetijobs',
            name='dir_used',
            field=models.TextField(blank=True),
        ),
    ]