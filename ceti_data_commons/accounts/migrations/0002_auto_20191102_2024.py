# Generated by Django 2.2.5 on 2019-11-03 00:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetails',
            new_name='UserProfile',
        ),
    ]
