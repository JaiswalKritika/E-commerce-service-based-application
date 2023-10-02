from django.db import models

class Users(models.Model):
    role=models.CharField(max_length=250,default="")
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    address = models.CharField(max_length=250,null=True,default="")
    city = models.CharField(max_length=250,null=True)
    country = models.CharField(max_length=250,null=True)
    postalcode = models.CharField(max_length=250,null=True)
    longitude = models.CharField(max_length=250,null=True)
    latitude = models.CharField(max_length=250,null=True)
    profilepic = models.CharField(max_length=250,null=True)
    idproof = models.CharField(max_length=250,null=True)
    created_date=models.DateTimeField(null=True)
    updated_date=models.DateTimeField(null=True)
    referel_code=models.CharField(max_length=250,default="")
    # wallet=models.CharField(max_length=255,blank=True,null=True)


class incomeHistory(models.Model):
    agent_id=models.CharField(max_length=250,default="")
    agent_amount = models.CharField(max_length=250)
    admin_amount = models.CharField(max_length=250)
    created_date=models.DateTimeField(null=True)

class Profile(models.Model):
    user=models.CharField(max_length=250,default="")
    email = models.CharField(max_length=250)
    otp = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)