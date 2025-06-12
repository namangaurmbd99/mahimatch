from django.db import models
from users.models import User
from django.utils.translation import gettext_lazy as _

class SubscriptionPlan(models.Model):
    class Interval(models.TextChoices):
        MONTH = 'MONTH', _('Monthly')
        YEAR = 'YEAR', _('Yearly')

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    interval = models.CharField(max_length=10, choices=Interval.choices)
    stripe_price_id = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_interval_display()})"

class UserSubscription(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', _('Active')
        PAST_DUE = 'PAST_DUE', _('Past Due')
        UNPAID = 'UNPAID', _('Unpaid')
        CANCELLED = 'CANCELLED', _('Cancelled')
        INCOMPLETE = 'INCOMPLETE', _('Incomplete')
        INCOMPLETE_EXPIRED = 'INCOMPLETE_EXPIRED', _('Incomplete Expired')
        TRIALING = 'TRIALING', _('Trialing')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=Status.choices)
    stripe_subscription_id = models.CharField(max_length=255)
    current_period_start = models.DateTimeField()
    current_period_end = models.DateTimeField()
    cancel_at_period_end = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email}'s {self.plan.name} Subscription"