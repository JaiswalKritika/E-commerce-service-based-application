from rest_framework import serializers
from members.Category import catego,SubCatego
from members.models import banner,AddService
from members.bookingModels import Bookings
from members.main_model import Users
# from members.login_models import *
from members.offer_model import offer
from members.main_model import Profile




class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=catego
        fields="__all__"


class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=SubCatego
        fields="__all__"

class BannerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=banner
        fields="__all__"

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        
        model=Bookings
        fields="__all__"


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=AddService
        fields="__all__"       

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Users
        fields="__all__"    

class AgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Users
        fields="__all__"        

class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Users
        fields="__all__"        

class PromoterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Users
        fields="__all__"   

 

class offerSerializer(serializers.ModelSerializer):
    class Meta:
        model=offer
        fields = "__all__"

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields = "__all__"