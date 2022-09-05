from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    CATEGORY_CHOICES = (
        ('100', '100 items'),
        ('200', '200 items'),
        ('300', '200 items'),
    )
    user_category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)