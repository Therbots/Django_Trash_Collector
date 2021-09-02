from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from .models import Employee
from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from datetime import *
import calendar

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    user = request.user
    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_employee = Employee.objects.get(user=user)
        employee_zip = logged_in_employee.zip_code
        today = date.today()
        str_day = (calendar.day_name[today.weekday()])

        Customer = apps.get_model('customers.Customer')
        all_customers = Customer.objects.filter(zip_code=employee_zip, weekly_pickup_day=str_day) | Customer.objects.filter(zip_code=employee_zip, one_time_pickup=today) and Customer.objects.filter(zip_code=employee_zip, suspend_start__gte=today, suspend_end__lte=today) | Customer.objects.filter(zip_code=employee_zip, suspend_start__isnull=True, suspend_end__isnull=True)
        return render(request, 'employees/index.html', {'all_customers' : all_customers})

    except:
        return render(request, 'employees/create.html')
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    
    


def create(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employee = Employee(user=user, zip_code=zip_code, name=name)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')

def confirm(request, user_id):
    Customer = apps.get_model('customers.Customer')
    customer_pickup = Customer.objects.get(pk=user_id)
    context = {
        'customer_pickup': customer_pickup
    }
    if request.method == "POST":
        customer_pickup.balance += 2
        customer_pickup.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/confirm.html', context)


