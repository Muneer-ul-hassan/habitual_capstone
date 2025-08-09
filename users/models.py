from django.db import models
from django.contrib.auth.models import AbstractUser
import pytz

class CustomUser(AbstractUser):
    TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]
    timezone = models.CharField(max_length=100, choices=TIMEZONE_CHOICES, default='UTC')
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_set', blank=True)
