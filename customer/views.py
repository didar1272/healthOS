from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from company.models import Phone
from .models import Customer
from .common import available_number

# Create your views here.


class CustomerRegistration(View):

    def post(self, request, *args, **kwargs):
        response_data = {}
        try:
            data = request.POST

            if not data['full_name'] or 'full_name' not in data:
                response_data = {
                    "result": "Something went wrong. Please check your full name input"
                }
                return JsonResponse(response_data)
            if not data['password'] or 'password' not in data:
                response_data = {
                    "result": "Something went wrong. Please check your password input"
                }
                return JsonResponse(response_data)

            if not data['email'] or 'email' not in data:
                response_data = {
                    "result": "Something went wrong. Please check your email input"
                }
                return JsonResponse(response_data)

            if not data['company'] or 'company' not in data:
                response_data = {
                    "result": "Something went wrong. Please check your Company input"
                }
                return JsonResponse(response_data)

            input_name = data['full_name']
            input_company = data['company']
            input_email = data['email']
            input_password = make_password(data['password'])

            if User.objects.filter(email=input_email).exists():

                response_data = {
                    "result": "User already exists"
                }
                return JsonResponse(response_data)

            assigned_number = available_number(input_company)

            if not assigned_number:
                response_data = {
                    "result": "No available Number to assign."
                }
                return JsonResponse(response_data)

            new_user = User()
            new_user.username = input_email
            new_user.password = input_password
            new_user.save()

            customer_obj = Customer()
            customer_obj.full_name = input_name
            customer_obj.customer_email = input_email
            customer_obj.customer_password = input_password
            customer_obj.customer_id = assigned_number

            customer_obj.primary_number = str(assigned_number)
            customer_obj.user = new_user

            customer_obj.save()

            Phone.objects.filter(
                phone_number=assigned_number).update(assigned_customer=customer_obj)

            response_data = {
                "result": "Registraiton Successful",
                "phone_number": F"Your assigned phone number is {assigned_number}"
            }
            return JsonResponse(response_data)
        except:
            response_data = {
                "result": "Something went wrong. Please check your inputs"
            }
            return JsonResponse(response_data)


class AddPhoneNumber(View):
    def post(self, request, *args, **kwargs):
        response_data = {}
        try:
            data = request.POST
            if not data['email'] or 'email' not in data:
                response_data = {
                    "result": "Something went wrong. Please check your email input"
                }
                return JsonResponse(response_data)

            if not data['company'] or 'company' not in data:
                response_data = {
                    "result": "Something went wrong. Please check your Company input"
                }
                return JsonResponse(response_data)

            input_company = data['company']
            input_email = data['email']

            assigned_number = available_number(input_company)

            if not assigned_number:
                response_data = {
                    "result": "No available Number to assign."
                }
                return JsonResponse(response_data)

            customer_obj = Customer.objects.filter(customer_email=input_email)

            if not customer_obj.exists():

                response_data = {
                    "result": "Customer does not exist."
                }
                return JsonResponse(response_data)

            Phone.objects.filter(phone_number=assigned_number).update(
                assigned_customer=customer_obj[0])

            response_data = {
                "result": "New Phone Number added Successfully.",
                "phone_number": F"Your assigned phone number is {assigned_number}"
            }

            return JsonResponse(response_data)

        except:
            response_data = {
                "result": "Something went wrong. Please check your inputs"
            }
            return JsonResponse(response_data)


class AddPrimaryNumber(View):
    pass


class SubscribeToPlan(View):
    pass


class CancelGoldPlan(View):
    pass
