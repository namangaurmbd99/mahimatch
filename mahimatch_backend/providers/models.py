from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _

class ProviderProfile(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', _('Pending Approval')
        APPROVED = 'APPROVED', _('Approved')
        REJECTED = 'REJECTED', _('Rejected')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='provider_profile')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    degree = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100, blank=True)
    years_of_experience = models.PositiveIntegerField(default=0)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    available_hours = models.JSONField(default=dict)  # {'monday': ['09:00-17:00'], ...}
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.specialization}"