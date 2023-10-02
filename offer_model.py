from django.db import models
class offer(models.Model):
    title=models.CharField(max_length=250,default="")
    description = models.CharField(max_length=250)
    Startdate_time = models.CharField(max_length=100, default="")
    Enddate_time = models.CharField(max_length=250, default="")
    coupon= models.CharField(max_length=250)
    discount = models.CharField(max_length=250)
    status = models.CharField(max_length=250,null=True,default="")
