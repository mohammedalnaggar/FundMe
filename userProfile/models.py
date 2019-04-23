from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.BigIntegerField(default='01000000000', null=True)
    picture = models.ImageField(upload_to='avatars/', default='avatars/avatar.png', null=True)
    birthday = models.DateField(default=timezone.now, null=True)
    facebook = models.URLField(default='www.facebook.com', null=True)
    country = models.CharField(default='Egypt', null=True, max_length=20)

    def __str__(self):
        return self.user.username
