# Generated by Django 2.2.4 on 2019-08-27 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_auto_20190825_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='user_id',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]