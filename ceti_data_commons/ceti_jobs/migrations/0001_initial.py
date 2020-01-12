# Generated by Django 2.2.5 on 2019-11-10 22:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CetiJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('job_title', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=0)),
                ('node', models.TextField(blank=True)),
                ('gpu', models.IntegerField(default=0)),
                ('latest_run', models.DateTimeField()),
                ('finished_at', models.DateTimeField()),
                ('dir_used', models.TextField(blank=True)),
                ('user_id', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
