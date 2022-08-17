from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from company.models import Company, Phone
from subscriptions.models import Subscribers, SubscriptionPlan
from .models import Customer
from .common import available_number
from django.utils.timezone import now

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
    def post(self, request, *args, **kwargs):
        response_data = {}
        try:
            data = request.POST
            if not data['email'] or 'email' not in data:
                response_data = {
                    "result": "Something went wrong. Please check your email input"
                }
                return JsonResponse(response_data)

            if not data['number'] or 'number' not in data:
                response_data = {
                    "result": "Something went wrong. Please check your Phone Number input"
                }
                return JsonResponse(response_data)

            input_number = data['number']
            input_email = data['email']

            customer_obj = Customer.objects.filter(customer_email=input_email)

            if not customer_obj.exists():

                response_data = {
                    "result": "Customer does not exist."
                }
                return JsonResponse(response_data)

            if not Phone.objects.filter(phone_number=input_number, assigned_customer=customer_obj[0]).exists():
                response_data = {
                    "result": "The Phone number does not belong to the Customer"
                }
                return JsonResponse(response_data)

            customer_obj[0].primary_number = input_number
            customer_obj[0].save()

            response_data = {
                "result": "Primary Phone Number added Successfully.",
            }

            return JsonResponse(response_data)

        except:
            response_data = {
                "result": "Something went wrong. Please check your inputs"
            }
            return JsonResponse(response_data)


class SubscribeToPlan(View):
    def post(self, request, *args, **kwargs):
        response_data = {}
        try:
            data = request.POST
            if not data['email'] or 'email' not in data:
                response_data = {
                    "result": "Something went wrong. Please check your email input"
                }
                return JsonResponse(response_data)

            if not data['number'] or 'number' not in data:
                response_data = {
                    "result": "Something went wrong. Please check your Phone Number input"
                }
                return JsonResponse(response_data)

            if not data['plan'] or 'plan' not in data:
                response_data = {
                    "result": "Something went wrong. Please check your Subcription plan input"
                }
                return JsonResponse(response_data)

            input_number = data['number']
            input_email = data['email']
            input_plan = data['plan']

            customer_obj = Customer.objects.filter(customer_email=input_email)

            if not customer_obj.exists():

                response_data = {
                    "result": "Customer does not exist."
                }
                return JsonResponse(response_data)

            phone_obj = Phone.objects.filter(
                phone_number=input_number, assigned_customer=customer_obj[0])

            if not phone_obj.exists():
                response_data = {
                    "result": "The Phone number does not belong to the Customer"
                }
                return JsonResponse(response_data)

            sub_obj = SubscriptionPlan(plan_name=input_plan)

            if not sub_obj.exists():
                response_data = {
                    "result": "The plan does not exist"
                }
                return JsonResponse(response_data)

            subscibers_obj = Subscribers(
                phone__company=phone_obj[0].company, customer=customer_obj[0])

            if subscibers_obj.exists():
                response_data = {
                    "result": "You already have subscribed to this company"
                }
                return JsonResponse(response_data)

            if customer_obj[0].balance >= sub_obj.plan_cost:
                new_subsciber_obj = Subscribers()
                new_subsciber_obj.customer = customer_obj[0]
                new_subsciber_obj.phone = phone_obj[0]
                new_subsciber_obj.active_plan = input_plan
                new_subsciber_obj.activation_date = now()
                new_subsciber_obj.charge_per_month = sub_obj.plan_cost
                new_subsciber_obj.save()

            response_data = {
                "result": F"You have Successfully subscribed to {input_plan} plan.",
            }

            return JsonResponse(response_data)

        except:
            response_data = {
                "result": "Something went wrong. Please check your inputs"
            }
            return JsonResponse(response_data)


class CancelGoldPlan(View):
    def post(self, request, *args, **kwargs):
        response_data = {}
        try:
            data = request.POST

            if not data['number'] or 'number' not in data:
                response_data = {
                    "result": "Something went wrong. Please check your Phone Number input"
                }
                return JsonResponse(response_data)

            input_number = data['number']
            plan_to_be_cancelled = 'GLOBALNET GOLD'

            phone_obj = Phone.objects.filter(
                phone_number=input_number)

            if not phone_obj.exists():
                response_data = {
                    "result": "The Phone number does not belong to the Customer"
                }
                return JsonResponse(response_data)

            subscibers_obj = Subscribers(
                phone=phone_obj[0], active_plan=plan_to_be_cancelled)

            if not subscibers_obj.exists():
                response_data = {
                    "result": "You already have not subscribed to this plan"
                }
                return JsonResponse(response_data)

            subscibers_obj.possible_end_date = now()
            subscibers_obj.save()

            response_data = {
                "result": F"You have Successfully cancelled Gold plan.",
            }

            return JsonResponse(response_data)

        except:
            response_data = {
                "result": "Something went wrong. Please check your inputs"
            }
            return JsonResponse(response_data)
