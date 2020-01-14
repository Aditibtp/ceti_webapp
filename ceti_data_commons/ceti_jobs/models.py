from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import pytz

class CetiJobs(models.Model):
    user_id = models.OneToOneField('auth.User', on_delete=models.DO_NOTHING, editable=False,)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    job_title = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
    node = models.TextField(default=0, blank=True)
    gpu = models.IntegerField(default=0)
    latest_run = models.DateTimeField(default=datetime.now, blank=True)
    finished_at = models.DateTimeField(default=datetime.now, blank=True)
    script_file = models.CharField(max_length=200)
    dir_used = models.TextField(blank=True)


    def __str__(self):
        return self.job_title