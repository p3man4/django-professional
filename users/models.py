from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    num_bags = models.PositiveIntegerField(null=True, blank=True)