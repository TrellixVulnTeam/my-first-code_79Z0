from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    users = models.OneToOneField(User)

    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.users.username