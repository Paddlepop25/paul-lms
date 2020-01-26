from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    reward_points = models.IntegerField(blank=False, default=0)
