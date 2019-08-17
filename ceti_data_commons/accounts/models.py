from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    g_id = models.CharField(max_length=50, blank=True, unique=True)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
