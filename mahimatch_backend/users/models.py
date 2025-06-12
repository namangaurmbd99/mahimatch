from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', _('Admin')
        PROVIDER = 'PROVIDER', _('Service Provider')
        CUSTOMER = 'CUSTOMER', _('Customer')
        SUBSCRIBER = 'SUBSCRIBER', _('Subscriber')
    
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CUSTOMER)
    firebase_uid = models.CharField(max_length=255, unique=True, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    avatar = models.URLField(blank=True)
    stripe_customer_id = models.CharField(max_length=255, blank=True, null=True)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email}'s Profile"