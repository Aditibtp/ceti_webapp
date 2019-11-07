from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    greyfish_active = models.BooleanField(default=False, null=True)
    account_type = models.IntegerField(default=1, null=True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
