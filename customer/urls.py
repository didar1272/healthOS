from django.urls import path

from customer.views import CustomerRegistration


urlpatterns = [
    path("register/", CustomerRegistration.as_view()),
]
