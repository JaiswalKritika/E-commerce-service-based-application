from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from members.serializers import *
from django.template import loader
from members.offer_model import offer

def getOfferApi(request):
        qs = offer.objects.all().values()
        serializer = offerSerializer(qs, many=True)
        return JsonResponse(data=serializer.data,safe=False)

def createOffer(request):
    return render(request,"createOffer.html")
def saveOffer(request):
    title = request.POST.get("title")
    description = request.POST.get("description")
    Startdate_time = request.POST.get("Startdate_time")
    Enddate_time = request.POST.get("Enddate_time")
    coupon = request.POST.get("coupon")
    discount = request.POST.get("discount")
    status = request.POST.get("status")
    o = offer()
    o.title=title
    o.description=description
    o.Startdate_time=Startdate_time
    o.Enddate_time=Enddate_time
    o.coupon=coupon
    o.discount=discount
    o.status=status
    o.created_date=datetime.datetime.now()
    o.save()
    return render(request,"createOffer.html")

def showOffer(request):
    offer_data=offer.objects.all().values
    return render(request,"showOffer.html",{"offer_data": offer_data})


def deleteOffer(request,id):
    delete1 = offer.objects.get(id=id)
    delete1.delete()
    return HttpResponseRedirect("/showOffer")

def updateOffer(request,id):
    data=offer.objects.get(id=id)
    return render(request,"updateOffer.html",{"data":data})


def Offer_update(request):
    id=request.POST.get("id")
    o=offer.objects.get(id=id)
    o.title=request.POST.get("title");
    o.description=request.POST.get("description");
    o.Startdate_time=request.POST.get("Startdate_time");
    o.Enddate_time=request.POST.get("Enddate_time");
    o.coupon=request.POST.get("coupon");
    o.discount=request.POST.get("discount");
    o.status=request.POST.get("status");
    o.updated_date=datetime.datetime.now()
    o.save()

    return HttpResponseRedirect("/showOffer")