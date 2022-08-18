from django.urls import path

from customer.views import CustomerRegistration, AddPhoneNumber, AddPrimaryNumber, SubscribeToPlan, CancelGoldPlan


urlpatterns = [
    path("register/", CustomerRegistration.as_view()),
    # form data input keys 'email', 'password', 'full_name', 'company'
    path("add/phone-number/", AddPhoneNumber.as_view()),
    # form data input keys 'email', 'company'
    path("add/primary-number/", AddPrimaryNumber.as_view()),
    # form data input keys 'email', 'number'
    path("subscribe/", SubscribeToPlan.as_view()),
    # form data input keys 'email', 'number', 'plan'
    path("cancel/gold-plan/", CancelGoldPlan.as_view()),
    # form data input keys 'number'
]
