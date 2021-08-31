from typing import Reversible
from django.urls import reverse
from django.db import models
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Customer
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_customer = Customer.objects.get(user=user)
    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        return render(request, 'customers/create.html')

    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key

    print(user)
    return render(request, 'customers/index.html')

def create(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zip_code')
        weekly_pickup_day = request.POST.get('weekly_pickup_day')
        new_customer = Customer(user=user, name=name, address=address, zip_code=zip_code, weekly_pickup_day=weekly_pickup_day)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    else:
        return render(request, 'customers/create.html')

def details(request):
    user = request.user
    single_user = Customer.objects.get(user=user)
    context = {
        'single_user' : single_user
    }
    return render(request, 'customers/details.html', context)

def weekly(request):
    pass
