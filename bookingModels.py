from django.db import models
from members.main_model import Users
from members.models import *

class Bookings(models.Model):
    #customer_id = models.ForeignKey(Users, on_delete=models.CASCADE,null=True)
    #partner_id = models.ForeignKey(Users, on_delete=models.CASCADE,null=True)
    appointment = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    partnerName = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    created_date=models.DateTimeField(null=True)
    updated_date=models.DateTimeField(null=True)

class Booking_items(models.Model):
    service_id=models.ForeignKey(AddService, related_name="user",on_delete=models.CASCADE)
    created_date=models.DateTimeField(null=True)
    status= models.CharField(max_length=200)