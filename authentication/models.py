from django.db import models
from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    NOT_AVAILABLE = 'NA'
    MANAGER = 'MANAGER'
    SALES = 'SALES'
    SUPPORT = 'SUPPORT'

    TEAM_CHOICES = [
        (MANAGER, 'Gestion'),
        (SALES, 'Vente'),
        (SUPPORT, 'Support'),
        (NOT_AVAILABLE, 'Inconnu')
    ]

    username = models.CharField(max_length=128, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    role = models.CharField(max_length=32, choices=TEAM_CHOICES)

    REQUIRED_FIELDS = ['role']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        group = Group.objects.get(name=self.role)
        group.user_set.add(self)
