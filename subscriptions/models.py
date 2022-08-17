from django.db import models
from customer.strings import SUBSCRIPTION_PLANS
from customer.models import Customer
from company.models import Company, Phone

# Create your models here.


class SubscriptionPlan(models.Model):
    plan_name = models.CharField(
        max_length=64, blank=True, null=True)
    plan_cost = models.IntegerField(blank=True, null=True)


class Subscribers(models.Model):
    active_plan = models.CharField(
        max_length=64, blank=True, null=True, choices=SUBSCRIPTION_PLANS)
    phone = models.ForeignKey(
        Phone, blank=True, null=True, on_delete=models.CASCADE, related_name='subscribed_phone')
    customer = models.ForeignKey(
        Customer, null=True, blank=True, on_delete=models.CASCADE, related_name='subscribed_customer')
    activation_date = models.DateTimeField(null=True, blank=True)
    possible_end_date = models.DateTimeField(null=True, blank=True)
    charge_per_month = models.IntegerField(null=True, blank=True)
