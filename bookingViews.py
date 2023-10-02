from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from members.bookingModels import Bookings
from django.template import loader
import datetime
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from members.serializers import BookingSerializer
from members.main_model import Users
from members.models import AddService

class BookingViewSet(viewsets.ModelViewSet):
    queryset=Bookings.objects.all()
    serializer_class=BookingSerializer







def createBooking(request):
    customer_id=Users.objects.filter(role='customer').values()
    # print(SubCategory_data)
    li=[]
    for x in customer_id:
        li.append(x)
    partner_id=Users.objects.filter(role='partner').values()
    return render(request,'createBooking.html',{"data":{"partner_id": partner_id, "titles":li}})

def saveBooking(request):
    b=Bookings()
    customer_id=Users.objects.get(id=request.POST.get("customer_id"))
    partner_id=Users.objects.get(id=request.POST.get("partner_id"))
    cost=request.POST.get("cost")
    status=request.POST.get("status")
    b.customer_id = customer_id
    b.partner_id = partner_id
    b.cost = cost
    b.status = status
    b.created_date=datetime.datetime.now()

    b.save()
    return render(request,"createBooking.html")

def showBooking(request):
    data = Bookings.objects.all().values()
    return render(request,"showBooking.html" ,{"data":data})

def deleteBooking(request,id):
    dele = Bookings.objects.get(id=id)
    dele.delete()
    data = Bookings.objects.all().values()
    return render(request, "showBooking.html",{"data":data})

def updateBooking(request,id):
    user = Bookings.objects.get(id=id)
    customer_id=Users.objects.filter(role='customer').values()
    # print(SubCategory_data)
    li=[]
    for x in customer_id:
        li.append(x)
    partner_id=Users.objects.filter(role='partner').values()
    return render(request, "updateBooking.html", {"user":user,"data":{"partner_id": partner_id, "titles":li}})



def updateBooking2(request):
    id = request.POST.get("id")
    b=Bookings.objects.get(id=id)
    customer_id=Users.objects.get(id=request.POST.get("customer_id"))
    partner_id=Users.objects.get(id=request.POST.get("partner_id"))
    cost=request.POST.get("cost")
    status=request.POST.get("status")
    b.customer_id = customer_id
    b.partner_id = partner_id
    b.cost = cost
    b.status = status
    b.updated_date=datetime.datetime.now()
    b.save()
    return HttpResponseRedirect("/showBooking")




def showBooking_items(request):
    data = Bookings.objects.all().values()
    return render(request,"showBooking_items.html" ,{"data":data})

def createAppconfig(request):
    data = Bookings.objects.all().values('cost')
    li = []
    li1 = []
    for i in range(0,len(data)):
        a=data[i]
        company_comission = int(a['cost'])*0.15
       
        agent_comission = int(a['cost'])*0.05
        
        company_comission1 = str(company_comission)
        agent_comission1 = str(agent_comission)
        li.append(company_comission1)
        li1.append(agent_comission1)
       
    return render(request,"createAppconfig.html" ,{"li":li,"li1":li1})