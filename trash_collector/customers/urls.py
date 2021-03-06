from os import name
from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('details/', views.details, name="details"),
    path('suspend/', views.suspend, name="suspend"),
    path('weekly/', views.weekly, name="weekly"),
    path('special/', views.special, name="special")
]
