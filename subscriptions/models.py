from django.db import models
from customer.strings import SUBSCRIPTION_PLANS
from customer.models import Customer
from company.models import Company

# Create your models here.


class SubscriptionPlan(models.Model):
    bronze = models.IntegerField(default=500)
    silver = models.IntegerField(default=750)
    gold = models.IntegerField(default=1500)


class Subscribers(models.Model):
    active_plan = models.CharField(
        max_length=64, blank=True, null=True, choices=SUBSCRIPTION_PLANS)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='subscribed_company')
    customer = models.ForeignKey(
        Customer, null=True, blank=True, on_delete=models.CASCADE, related_name='subscribed_customer')
    activation_date = models.DateTimeField(null=True, blank=True)
    possible_end_date = models.DateTimeField(null=True, blank=True)
    charge_per_month = models.ForeignKey(
        SubscriptionPlan, null=True, blank=True, on_delete=models.CASCADE, related_name='subscription_money')
