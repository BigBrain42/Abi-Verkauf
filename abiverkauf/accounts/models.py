from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Kunde'),
        ('seller', 'Verkäufer'),
        ('admin', 'Administrator'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    def is_seller(self):
        return self.role == 'seller'

    def is_admin_user(self):
        return self.role == 'admin' or self.is_superuser
