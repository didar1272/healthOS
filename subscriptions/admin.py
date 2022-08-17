from django.contrib import admin
from .models import Subscribers, SubscriptionPlan

# Register your models here.

admin.site.register(Subscribers)
admin.site.register(SubscriptionPlan)
