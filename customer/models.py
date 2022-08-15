from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from .strings import SUBSCRIPTION_PLANS

# Create your models here.


def number_uniqness(value):
    if value:
        print(value)


class Customer(models.Model):
    customer_id = models.CharField(
        max_length=16, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=64)
    primary_number = models.CharField(max_length=16, null=True)
    customer_email = models.EmailField(
        max_length=50, unique=True)
    customer_password = models.CharField(
        max_length=128)
    balance = models.IntegerField(default=1000)
    current_plan = models.CharField(
        max_length=64, blank=True, choices=SUBSCRIPTION_PLANS)
    registrasion_datetime = models.DateTimeField(default=now, editable=False)
    # testfield = models.CharField(max_length=64, null=True)
