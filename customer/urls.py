from django.urls import path

from customer.views import CustomerRegistration, AddPhoneNumber, AddPrimaryNumber, SubscribeToPlan, CancelGoldPlan


urlpatterns = [
    path("register/", CustomerRegistration.as_view()),
    path("add/phone-number/", AddPhoneNumber.as_view()),
    path("add/primary-number/", AddPrimaryNumber.as_view()),
    path("subscribe/", SubscribeToPlan.as_view()),
    path("cancel/gold-plan/", CancelGoldPlan.as_view()),
]
