from django.db import models
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE),
    address = models.CharField(max_length=50),
    zip_code = models.CharField(max_length=50),
    balance = models.IntegerField(max_length=50),
    weekly_pickup_day = models.CharField(max_length=50),
    one_time_pickup = models.DateField(null=True),
    suspend_start = models.DateField(null=True),
    suspend_end = models.DateField(null=True)

    def __str__(self):
        return self.name