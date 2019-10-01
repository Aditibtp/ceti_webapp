from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

import uuid

class Storage(models.Model):
    storage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    user_id = models.OneToOneField('auth.User', on_delete=models.CASCADE, editable=False,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.storage_id

