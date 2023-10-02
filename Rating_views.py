import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from members.main_model import Users
from members.models import Rating
from rest_framework import viewsets








def createRating(request):
    customer_data = Users.objects.filter(role='customer')
    partner_data = Users.objects.filter(role='partner')
    return render(request, "createRating.html",{"data":{"customer_data": customer_data, "partner_data":partner_data}})

def saveRating(request):
    customer_data=request.POST.get("data1")
    partner_data=request.POST.get("data2")
    rating = request.POST.get("rating")
    reply = request.POST.get("reply")
    
    u = Rating()
    u.data1 = customer_data
    u.data2 = partner_data
    u.rating = rating
    u.reply = reply
    u.created_date=datetime.datetime.now()
    u.save()
    return render(request,"createRating.html")

def showRating(request):
    data = Rating.objects.all().values()
    return render(request,"showRating.html",{"data":data})

def deleteRating(request,id):
    dele = Rating.objects.get(id=id)
    dele.delete()
    u = Rating()
    data = Rating.objects.all().values()
    return render(request, "showRating.html", {"data": data})
