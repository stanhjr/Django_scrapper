from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    CATEGORY_CHOICES = (
        ('100', '100 items'),
        ('200', '200 items'),
        ('300', '300 items'),
    )
    user_category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)

    def get_number_items(self):
        return int(self.user_category)


class OlxModel(models.Model):
    tittle = models.CharField(max_length=2000)
    name = models.CharField(max_length=2000)
    src = models.CharField(max_length=2000)
    price_grv = models.IntegerField()
    price_dollar = models.IntegerField()

    def __str__(self):
        return f"{self.tittle} by {self.name}"

    def get_price_grv(self):
        return self.price_grv / 100

    def get_price_dollar(self):
        return self.price_dollar / 100

    class Meta:
        ordering = ("price_grv",)
