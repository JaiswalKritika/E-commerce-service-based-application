from django.db import models
from members.Category import SubCatego, catego
from members.main_model import Users
from tinymce.models import HTMLField

class AddService(models.Model):
        categories=models.ForeignKey(catego, on_delete=models.CASCADE)
        SubCategories=models.ForeignKey(SubCatego, on_delete=models.CASCADE)
        title=models.CharField(max_length=50)
        price=models.CharField(max_length=500)
        discount=models.CharField(max_length=50)
        time=models.CharField(max_length=500)
        image=models.CharField(max_length=250)
        offer=models.CharField(max_length=250,default="",null=True)
        value=models.CharField(max_length=250,default="",null=True)
class banner(models.Model):
        title=models.CharField(max_length=50)
        description=HTMLField(max_length=250)
        created_date=models.DateTimeField(null=True)
        updated_date=models.DateTimeField(null=True)
        banner_image=models.CharField(max_length=250,default="",null=True)

class Rating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    data1 = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    data2=models.CharField(max_length=200,default="",null=True)
    rating = models.IntegerField(choices=RATING_CHOICES,default="",null=True)
    reply = models.CharField(max_length=200)
    created_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(null=True)



class Terms(models.Model):
    terms=HTMLField(max_length=50,default="",null=True)
        

class createpackages(models.Model):
    Title = models.CharField(max_length=50,null=True)
    Description= models.CharField(max_length=50,null=True)
    StartDate = models.CharField(max_length=60,null=True)
    EndDate = models.CharField(max_length=50,null=True)
    PackageName = models.CharField(max_length=50,null=True)
    PackageCost = models.CharField(max_length=50,null=True)
    NumberOfPartner = models.CharField(max_length=50,null=True)
    ReferalCode = models.CharField(max_length=50,null=True)
    package_image=models.CharField(max_length=250,default="",null=True)
