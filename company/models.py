from django.db import models

from customer.models import Customer

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=128, primary_key=True)

    def __str__(self):
        return self.name


class Phone(models.Model):
    phone_number = models.CharField(max_length=16, unique=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='phone_company')
    assigned_customer = models.ForeignKey(
        Customer, null=True, on_delete=models.CASCADE, related_name='phone_customer')
