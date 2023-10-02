from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from members.models import AddService, banner, Terms ,createpackages
from django.template import RequestContext, loader
from members.main_model import Users,incomeHistory,Profile
from members.Category import catego , SubCatego
# from members.login_models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login as auth_login
import datetime
from django.core.mail import send_mail,EmailMultiAlternatives
from members.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
import random
import http.client
from django.conf import settings
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
#===========================================================================API

    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=catego.objects.all()
    serializer_class=CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset=SubCatego.objects.all()
    serializer_class=SubCategorySerializer

    @action(detail=True,methods=['get'])
    def categories(self,request,pk=None):
        try:
            subcategory=SubCatego.objects.get(pk=pk)
            category=catego.objects.filter(subcategory=subcategory)
            category_serializer=CategorySerializer(category,many=True,context={'request':request})
            return Response(category_serializer.data)
        except Exception as e:
            return Response({'message':'Not exist'})
class BannerViewSet(viewsets.ModelViewSet):
    queryset=banner.objects.all()
    serializer_class=BannerSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset=AddService.objects.all()
    serializer_class=ServiceSerializer
    @action(detail=True,methods=['get'])
    def service(self,request,pk=None):
        try:
            category=catego.objects.get(pk=pk)
            subcategory=SubCatego.objects.get(pk=pk)
            service=AddService.objects.filter(subcategory=subcategory,category=category)
            service_serializer=CategorySerializer(service,many=True,context={'request':request})
            return Response(service_serializer.data)
        except Exception as e:
            return Response({'message':'Not exist'})


class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Users.objects.filter(role='customer')
    serializer_class=CustomerSerializer

class AgentViewSet(viewsets.ModelViewSet):
    queryset=Users.objects.filter(role='agent')
    serializer_class=AgentSerializer

class PartnerViewSet(viewsets.ModelViewSet):
    queryset=Users.objects.filter(role='partner')
    serializer_class=PartnerSerializer

class PromoterViewSet(viewsets.ModelViewSet):
    queryset=Users.objects.filter(role='promoter')
    serializer_class=PromoterSerializer
    
class loginViewSet(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=loginSerializer
    @action(detail=True,methods=['get'])
    def login(self,request,pk=None):
        try:
            user=User.objects.get(pk=pk)
            profile=Profile.objects.filter(user=user)
            login_serializer=CategorySerializer(profile,many=True,context={'request':request})
            return Response(login_serializer.data)
        except Exception as e:
            return Response({'message':'Not exist'})




#===========================================================================terms&condition


def terms(request):
    return render(request,'terms.html')

def saveTerms(request):
    terms = request.POST.get("description")
    print(terms)
    t=Terms()
    t.terms=terms
    t.save()
    return render(request,'terms.html')


#======================================================================================================sighnup

def signUp(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        check_user=User.objects.filter(email=email).first()
        check_profile=Profile.objects.filter(mobile=mobile).first()
        if check_user or check_profile:
            context={'message':'User already exist','class':'danger'}
            return render(request,'signUp.html',context)
        user=User.objects.create_user(username,email)
        user.save()
        otp=random.randint(1111,9999)
        profile=Profile(user=user,mobile=mobile,otp=otp,email=email)
        profile.save()
        
        subject="otp verification"
        message=str(otp)
        email_from=settings.EMAIL_HOST_USER
        recipient_list=user.email

        send_mail(subject,message,email_from,[recipient_list],fail_silently=False)

        
        
    return render(request,"signUp.html")

         
def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        otp=int(request.POST.get('otp'))
        user=Profile.objects.filter(email=email).first()
        if user is None:
            context={'message':'User not found','class':'danger'}
            return render(request,'login.html',context)
        verify_otp=int(user.otp)
        if otp == verify_otp:
            return redirect('homePage')
        else:
            context={'message':'Wrong Otp','class':'danger'}
            return render(request,'login.html',context)
    return render(request,'login.html')
        

        

def signOut(request):
    logout(request)
    return redirect('signIn')

#===========================================================================homepage
def homePage(request):
    customer = Users.objects.filter(role='customer')
    customer_count = customer.count()
    service = AddService.objects.all()
    service_count = service.count()
    agent = Users.objects.filter(role='Agent')
    agent_count = agent.count()
    category = catego.objects.all()
    category_count = category.count()

    Sub_cat = SubCatego.objects.all()
    sub_cat_count = Sub_cat.count()

    promoter = Users.objects.filter(role='promoter')
    promoter_count = promoter.count()

    context = {
        'customer_count':customer_count,
        'service_count':service_count,
        'agent_count':agent_count,
        'category_count':category_count,
        'sub_cat_count':sub_cat_count,
        'promoter_count':promoter_count
    }
    return render(request,"homePage.html",context)


#============================================================================service


def createService(request):
    SubCategory_data=SubCatego.objects.all().values()
    # print(SubCategory_data)
    li=[]
    for x in SubCategory_data:
        li.append(x)
    category_data=catego.objects.all().values()

    return render(request, "createService.html", {"data":{"category_data": category_data, "titles":li}})
    

def saveService(request):
    global price
    u = AddService()
    categories=catego.objects.get(id=request.POST.get("categories"))
    SubCategories=SubCatego.objects.get(id=request.POST.get("SubCategories"))
    title = request.POST.get("title")
    price = request.POST.get("price")
    discount = request.POST.get("discount")
    time = request.POST.get("time")
    image = request.POST.get("image")
    offer = request.POST.get("offer")
    value = request.POST.get("value")


    u.categories = categories
    u.SubCategories = SubCategories
    u.title = title
    u.price = price
    u.discount = discount
    u.time = time
    u.image = image
    u.offer = offer
    u.value = value
    u.created_date=datetime.datetime.now()
    u.save()
    return render(request,"createService.html")

def showService(request):
    data = AddService.objects.all().values()
    return render(request,"service.html",{"data":data})

def deleteService(request,id):
    dele = AddService.objects.get(id=id)
    dele.delete()
    u = AddService()
    data = AddService.objects.all().values()
    return render(request, "service.html", {"data": data})

def updateService(request,id):
    
    SubCategory_data=SubCatego.objects.all().values()
    li=[]
    for x in SubCategory_data:
        li.append(x)
    category_data=catego.objects.all().values()
    
    user=AddService.objects.get(id=id)
    return render(request,"updateService.html", {"user":user,"data":{"category_data": category_data, "titles":li}})

def updateService1(request):
    id=request.POST.get("id")
    u = AddService.objects.get(id=id)
    categories=catego.objects.get(id=request.POST.get("categories"))
    SubCategories=SubCatego.objects.get(id=request.POST.get("SubCategories"))


    title = request.POST.get("title")
    price = request.POST.get("price")
    discount = request.POST.get("discount")
    time = request.POST.get("time")
    image = request.POST.get("image")
    offer = request.POST.get("offer")
    value = request.POST.get("value")

    u.categories = categories
    u.SubCategories = SubCategories
    u.title = title
    u.price = price
    u.discount = discount
    u.time = time
    u.image = image
    u.offer = offer
    u.value = value
    u.updated_date=datetime.datetime.now()
    u.save()
    return HttpResponseRedirect("/showService")

#====================================================================================INCOME HISTORY Views
list=[]
def incomeHistory(request):
    amount=AddService.objects.get(price=request.POST.get("price"))
    print(amount)
    for i in amount:
        cal=i * 0.15
    data=list.extend(cal)
    
    return render(request, "incomeHistory.html",{data:'data'})






#====================================================================================Customer Views

def creatCustomer(request):
    return render(request,"createCustomer.html")

def saveCustomer(request):
    c = Users()
    role = request.POST.get("role")
    email = request.POST.get("email")
    password = request.POST.get("password")
    name = request.POST.get("name")
    contact = request.POST.get("contact")
    address = request.POST.get("address")
    city = request.POST.get("city")
    country = request.POST.get("country")
    postalcode = request.POST.get("postalcode")
    longitude = request.POST.get("longitude")
    latitude = request.POST.get("latitude")
    profilepic = request.POST.get("profilepic")
    idproof = request.POST.get("idproof")
    c.role = role
    c.email = email
    c.password = password
    c.name = name
    c.contact = contact
    c.address = address
    c.city = city
    c.country = country
    c.postalcode = postalcode
    c.longitude = longitude
    c.latitude = latitude
    c.profilepic = profilepic
    c.idproof = idproof
    c.created_date=datetime.datetime.now()

    c.save()
    return render(request,"createCustomer.html")

def showCustomer(request):
    data = Users.objects.filter(role='customer')
    return render(request, "showCustomer.html", {"data": data})

def deleteCustomer(request,id):
    assert isinstance(id, object)
    dele = Users.objects.get(id=id)
    dele.delete()
    data = Users.objects.filter(role='customer')
    return render(request, "showCustomer.html", {"data": data})

def updateCustomer(request,id):
    user = Users.objects.get(id=id)
    return render(request, "updateCustomer.html", {"user": user})

def updateCustmer2(request):
    id = request.POST.get("id")
    c = Users.objects.get(id=id)
    email = request.POST.get("email")
    password = request.POST.get("password")
    name = request.POST.get("name")
    contact = request.POST.get("contact")
    address = request.POST.get("address")
    city = request.POST.get("city")
    country = request.POST.get("country")
    postalcode = request.POST.get("postalcode")
    longitude = request.POST.get("longitude")
    latitude = request.POST.get("latitude")
    profilepic = request.POST.get("profilepic")
    idproof = request.POST.get("idproof")
    c.email = email
    c.password = password
    c.name = name
    c.contact = contact
    c.address = address
    c.city = city
    c.country = country
    c.postalcode = postalcode
    c.longitude = longitude
    c.latitude = latitude
    c.profilepic = profilepic
    c.idproof = idproof
    c.updated_date=datetime.datetime.now()

    c.save()
    return HttpResponseRedirect("/showCustomer")


#===================================================================================partner

def createPartner(request):
    return render(request , "createPartner.html")

def savePartner(request):
    c = Users()
    role = request.POST.get("role")
    email = request.POST.get("email")
    password = request.POST.get("password")
    name = request.POST.get("name")
    contact = request.POST.get("contact")
    address = request.POST.get("address")
    city = request.POST.get("city")
    country = request.POST.get("country")
    postalcode = request.POST.get("postalcode")
    longitude = request.POST.get("longitude")
    latitude = request.POST.get("latitude")
    profilepic = request.POST.get("profilepic")
    idproof = request.POST.get("idproof")
    c.role = role
    c.email = email
    c.password = password
    c.name = name
    c.contact = contact
    c.address = address
    c.city = city
    c.country = country
    c.postalcode = postalcode
    c.longitude = longitude
    c.latitude = latitude
    c.profilepic = profilepic
    c.idproof = idproof
    c.created_date=datetime.datetime.now()

    c.save()
    return render(request,"createPartner.html")

def showPartner(request):
    data = Users.objects.filter(role='partner')
    return render(request, "showPartner.html", {"data": data})

def deletePartner(request,id):
    assert isinstance(id, object)
    dele = Users.objects.get(id=id)
    dele.delete()
    data = Users.objects.filter(role='partner')
    return render(request, "showPartner.html", {"data": data})

def updatePartner(request,id):
    user = Users.objects.get(id=id)
    return render(request, "updatePartner.html", {"user": user})

def updatePartner2(request):
    id = request.POST.get("id")
    c = Users.objects.get(id=id)
    email = request.POST.get("email")
    password = request.POST.get("password")
    name = request.POST.get("name")
    contact = request.POST.get("contact")
    address = request.POST.get("address")
    city = request.POST.get("city")
    country = request.POST.get("country")
    postalcode = request.POST.get("postalcode")
    longitude = request.POST.get("longitude")
    latitude = request.POST.get("latitude")
    profilepic = request.POST.get("profilepic")
    idproof = request.POST.get("idproof")
    c.email = email
    c.password = password
    c.name = name
    c.contact = contact
    c.address = address
    c.city = city
    c.country = country
    c.postalcode = postalcode
    c.longitude = longitude
    c.latitude = latitude
    c.profilepic = profilepic
    c.idproof = idproof
    c.updated_date=datetime.datetime.now()

    c.save()
    return HttpResponseRedirect("/showPartner")








#====================================================================================Agent Views
def createAgent(request):
    return render(request,"createAgent.html")

def saveAgent(request):
    role = request.POST.get("role")
    email = request.POST.get("email")
    password = request.POST.get("password")
    name = request.POST.get("name")
    contact = request.POST.get("contact")
    address = request.POST.get("address")
    city = request.POST.get("city")
    country = request.POST.get("country")
    postalcode = request.POST.get("postalcode")
    longitude = request.POST.get("longitude")
    latitude = request.POST.get("latitude")
    profilepic = request.POST.get("profilepic")
    idproof = request.POST.get("idproof")

    c = Users()
    c.role = role 
    c.email = email
    c.password = password
    c.name = name
    c.contact = contact
    c.address = address
    c.city = city
    c.country = country
    c.postalcode = postalcode
    c.longitude = longitude
    c.latitude = latitude
    c.profilepic = profilepic
    c.idproof = idproof
    c.created_date=datetime.datetime.now()

    c.save()
    return render(request,"createAgent.html")

def showAgent(request):
    data = Users.objects.filter(role='Agent')
    return render(request,"showAgent.html",{"data":data})
def updateAgent(request,id):
    agent=Users.objects.get(id=id)
    return render(request,"updateAgent.html",{"agent":agent})

def save_updateAgent(request):
    id=request.POST.get("id")
    c= Users.objects.get(id=id)
    email = request.POST.get("email")
    password = request.POST.get("password")
    name = request.POST.get("name")
    contact = request.POST.get("contact")
    address = request.POST.get("address")
    city = request.POST.get("city")
    country = request.POST.get("country")
    postalcode = request.POST.get("postalcode")
    longitude = request.POST.get("longitude")
    latitude = request.POST.get("latitude")
    profilepic = request.POST.get("profilepic")
    idproof = request.POST.get("idproof")\
    
    c.email = email
    c.password = password
    c.name = name
    c.contact = contact
    c.address = address
    c.city = city
    c.country = country
    c.postalcode = postalcode
    c.longitude = longitude
    c.latitude = latitude
    c.profilepic = profilepic
    c.idproof = idproof
    c.updated_date=datetime.datetime.now()

    c.save()
    return HttpResponseRedirect("/showAgent")

def deleteAgent(request,id):
    dele = Users.objects.get(id=id)
    dele.delete()
    data = Users.objects.filter(role='Agent')
    return render(request, "showAgent.html", {"data": data})


#====================================================================================Promoter Views
def createPromoter(request):
    return render(request,"createPromoter.html")

def savePromoter(request):
    role = request.POST.get("role")
    email = request.POST.get("email")
    password = request.POST.get("password")
    name = request.POST.get("name")
    contact = request.POST.get("contact")
    address = request.POST.get("address")
    city = request.POST.get("city")
    country = request.POST.get("country")
    postalcode = request.POST.get("postalcode")
    longitude = request.POST.get("longitude")
    latitude = request.POST.get("latitude")
    profilepic = request.POST.get("profilepic")
    idproof = request.POST.get("idproof")
    c = Users()
    c.role = role 
    c.email = email
    c.password = password
    c.name = name
    c.contact = contact
    c.address = address
    c.city = city
    c.country = country
    c.postalcode = postalcode
    c.longitude = longitude
    c.latitude = latitude
    c.profilepic = profilepic
    c.idproof = idproof
    c.created_date=datetime.datetime.now()

    c.save()
    return render(request,"createPromoter.html")

def showPromoter(request):
    data = Users.objects.filter(role='promoter')
    return render(request,"showPromoter.html",{"data":data})

def updatePromoter(request,id):
    promoter=Users.objects.get(id=id)
    print(promoter)
    return render(request,"updatePromoter.html",{"promoter":promoter})

def save_updatePromoter(request):
    id=request.POST.get("id")
    c= Users.objects.get(id=id)
    email = request.POST.get("email")
    password = request.POST.get("password")
    name = request.POST.get("name")
    contact = request.POST.get("contact")
    address = request.POST.get("address")
    city = request.POST.get("city")
    country = request.POST.get("country")
    postalcode = request.POST.get("postalcode")
    longitude = request.POST.get("longitude")
    latitude = request.POST.get("latitude")
    profilepic = request.POST.get("profilepic")
    idproof = request.POST.get("idproof")
    
    c.email = email
    c.password = password
    c.name = name
    c.contact = contact
    c.address = address
    c.city = city
    c.country = country
    c.postalcode = postalcode
    c.longitude = longitude
    c.latitude = latitude
    c.profilepic = profilepic
    c.idproof = idproof
    c.updated_date=datetime.datetime.now()

    c.save()
    return HttpResponseRedirect("/showPromoter")

def deletePromoter(request,id):
    dele = Users.objects.get(id=id)
    dele.delete()
    data = Users.objects.filter(role='promoter')
    return render(request, "showPromoter.html", {"data": data})





#====================================================================================Category Views

def createCategory(request):
    template = loader.get_template('createCategory.html')
    return HttpResponse(template.render())
def saveData(request):
    title = request.POST.get("title")
    description = request.POST.get("description")
    image = request.POST.get("image")
    print(title)
    print(description)
    print(image)
    c=catego()
    c.title=title;
    c.description = description;
    c.image=image;
    c.created_date=datetime.datetime.now()
    c.save()
    template = loader.get_template('createCategory.html')
    return HttpResponse(template.render())

def showCategory(request):
    cat = catego.objects.all().values()
    return render(request, "showCategory.html", {"cat": cat})

def update(request):
    id=request.POST.get("id")
    u=catego.objects.get(id=id)
    u.title= request.POST.get("title");
    u.description=request.POST.get("description");
    u.image=request.POST.get("image");
    u.updated_date=datetime.datetime.now()
    u.save()
    return HttpResponseRedirect("/showCategory")
def delete(request,id):
    delete1 = catego.objects.get(id=id)
    delete1.delete()
    return HttpResponseRedirect("/showCategory")

def updateCategory(request,id):
    cat=catego.objects.get(id=id)
    return render(request,"updateCategory.html",{"cat":cat})




#====================================================================================SubCategory Views

def createSubCategory(request):
    category_data=catego.objects.all().values()
    
    return render(request, "createSubCategory.html", {"category_data": category_data})
def saveDataSubCategory(request):
    catgoobj=catego.objects.get(id=request.POST.get("category_Id"))
    title = request.POST.get("title")
    description = request.POST.get("description")
    image = request.POST.get("image")
    print(title)
    print(description)
    print(image)
    c=SubCatego()
    c.category_Id=catgoobj;
    c.title=title;
    c.description = description;
    c.Subcategory_image=image;
    c.created_date=datetime.datetime.now()
    c.save()
    
    template = loader.get_template('createSubCategory.html')
    return HttpResponse(template.render())


def showSubCategory(request):
    Sub_cat = SubCatego.objects.all().values()
    return render(request, "showSubCategory.html", {"Sub_cat": Sub_cat})

def Sub_update(request):
    id=request.POST.get("id")
    u=SubCatego.objects.get(id=id)
    catgoobj=catego.objects.get(id=request.POST.get("category_Id"))
    title= request.POST.get("title");
    description=request.POST.get("description");
    Subcategory_image=request.POST.get("image");
    u.category_Id=catgoobj;
    u.title=title;
    u.description=description;
    u.Subcategory_image=Subcategory_image;
    u.updated_date=datetime.datetime.now()
    u.save()
    return HttpResponseRedirect("/showSubCategory")

def Sub_delete(request,id):
    delete1 = SubCatego.objects.get(id=id)
    delete1.delete()
    return HttpResponseRedirect("/showSubCategory")

def updateSubCategory(request,id):
    category_data=catego.objects.all().values()
    Sub_cat=SubCatego.objects.get(id=id)
    return render(request,"updateSubCategory.html",{"Sub_cat":Sub_cat,"category_data": category_data})


#====================================================================================Banner Views
def createBanner(request):
    return render(request, "createBanner.html")
def saveBanner(request):
    title = request.POST.get("title")
    description = request.POST.get("description")
    banner_image = request.POST.get("banner_image")
   
    c=banner()
    c.title=title;
    c.description = description;
    c.banner_image=banner_image;
    c.created_date=datetime.datetime.now()
    c.save()
    
    template = loader.get_template('createBanner.html')
    return HttpResponse(template.render())


def showBanner(request):
    data = banner.objects.all().values()
    return render(request, "showBanner.html", {"data": data})

def saveUpdatebanner(request):
    id=request.POST.get("id")
    u=banner.objects.get(id=id)
    title= request.POST.get("title");
    description=request.POST.get("description");
    banner_image=request.POST.get("banner_image");
    u.title=title;
    u.description=description;
    u.banner_image=banner_image;
    u.updated_date=datetime.datetime.now()
    u.save()
    return HttpResponseRedirect("/showBanner")

def deleteBanner(request,id):
    deletebanner = banner.objects.get(id=id)
    deletebanner.delete()
    return HttpResponseRedirect("/showBanner")

def updateBanner(request,id):
    data=banner.objects.get(id=id)
    return render(request,"updateBanner.html",{"data":data})



#===================================================================================Package Views

def Createpackage(request):
    return render(request, "createPackage.html")

def save(request):
    u = createpackages()
    Title = request.POST.get("Title")
    Description = request.POST.get("Description")
    StartDate = request.POST.get("StartDate")
    EndDate = request.POST.get("EndDate")
    PackageName = request.POST.get("PackageName")
    PackageCost = request.POST.get("PackageCost")
    NumberOfPartner = request.POST.get("NumberOfPartner")
    ReferalCode  = request.POST.get("ReferalCode")
    package_image=request.POST.get("package_image")
    u.Title=Title
    u.Description=Description
    u.StartDate=StartDate
    u.EndDate=EndDate
    u.PackageName=PackageName
    u.PackageCost=PackageCost
    u.NumberOfPartner=NumberOfPartner
    u.ReferalCode=ReferalCode
    u.save()
    return render(request, "createPackage.html")


def showCreatePackageInfo(request):
    data = createpackages.objects.all().values()
    return render(request, "showCreatePackage.html", {"data": data})

def deletePackage(request, id):
    del1 = createpackages.objects.get(id=id)
    del1.delete()
    data = createpackages.objects.all().values()
    return render(request, "showCreatePackage.html", {"data": data})

def updatePackage(request, id):
    user = createpackages.objects.get(id=id)
    return render(request, "UpdatePackage.html", {"user": user})

def updatedPackage(request):
    id = request.POST.get("id")
    u = createpackages.objects.get(id=id)
    u.Title = request.POST.get("Title")
    u.Description = request.POST.get("Description")
    u.StartDate = request.POST.get("StartDate")
    u.EndDate = request.POST.get("EndDate")
    u.PackageName = request.POST.get("PackageName")
    u.PackageCost = request.POST.get("PackageCost")
    u.NumberOfPartner = request.POST.get("NumberOfPartner")
    u.ReferalCode  = request.POST.get("ReferalCode")
    u.package_image=request.POST.get("package_image")
    u.save()
    data = createpackages.objects.all().values()
    return render(request, "showCreatePackage.html", {"data": data})





