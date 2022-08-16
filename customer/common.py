from company.models import Phone

# functions for common purpose usage


def available_number(input_company):
    number = Phone.objects.filter(
        company__name=input_company, assigned_customer=None)
    if len(number) > 0:
        return number[0]
    else:
        return None
