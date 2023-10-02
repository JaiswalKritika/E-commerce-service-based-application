
from django.contrib import admin
from django.urls import include, path
from . import views
from . import offer_view
from . import bookingViews
from . import Rating_views
from .form import MyPasswordResetForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView , PasswordChangeDoneView , LogoutView , PasswordResetView , PasswordResetConfirmView,PasswordResetDoneView
from django.conf import settings
from django.conf.urls.static import static
from members.views import *
from rest_framework import routers
from members.bookingViews import BookingViewSet

router=routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'subcategory', SubCategoryViewSet)
router.register(r'banner', BannerViewSet)
router.register(r'booking', BookingViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'agent', AgentViewSet)
router.register(r'partner', PartnerViewSet)
router.register(r'promoter', PromoterViewSet)
router.register(r'login', loginViewSet)







urlpatterns = [
#======================================================================================API

    path('api/',include(router.urls)),
    # path('loginView/',views.loginView , name='loginView'),
    path('getOfferApi/', offer_view.getOfferApi, name='getOfferApi'),
    
#======================================================================================terms and condition  
    path('tinymce/', include('tinymce.urls')),
    path('terms/', views.terms, name='terms'),
    path('saveTerms/', views.saveTerms, name='saveTerms'),
#======================================================================================signin/signup
    #path("", views.signIn, name='signIn'),
    path('signUp/', views.signUp, name='signUp'),
    path('signOut/', views.signOut, name='signOut'),
    path ('', views.login, name='login'),
    # path ('login_otp/', views.login_otp, name='login_otp'),

#=========================================================================================forgotPassword
    path('reset-password/', PasswordResetView.as_view(template_name='reset_password.html',form_class=MyPasswordResetForm) , name='reset_password'),
    path('password-reset-confirm/<uidb64>/token/', PasswordResetConfirmView.as_view(),name='password_reset_Sconfirm'),
    path('password-reset-done/', PasswordResetDoneView.as_view(template_name='reset_password_done.html') , name="password_reset_done"),
#========================================================================================homepage
    path('homePage/',views.homePage, name = 'homePage'),
#=========================================================================================service
    path('createService/',views.createService, name='createService'),
    path('saveService/',views.saveService, name='saveService'),
    path('showService/',views.showService, name = 'showService'),
    path('deleteService/<int:id>',views.deleteService, name = 'deleteService'),
    path('updateService1/', views.updateService1, name='updateService1'),
    path('update-user/<int:id>', views.updateService, name='update-user'),

##=======================================================================================Custmer url
    path('creatCustomer/', views.creatCustomer, name='creatCustomer'),
    path('saveCustomer/', views.saveCustomer, name='saveCustomer'),
    path('showCustomer/',views.showCustomer, name='showCustomer'),
    path('deleteCustomer/<int:id>',views.deleteCustomer,name='deleteCustomer'),
    path('updateCustomer/<int:id>',views.updateCustomer,name='updateCustomer'),
    path('updateCustmer2/',views.updateCustmer2,name='updateCustmer2'),


#========================================================================================Partner url
    path('createPartner/', views.createPartner , name='createPartner'),
    path('savePartner/' , views.savePartner , name='savePartner'),
    path('showPartner/', views.showPartner , name='showPartner'),
    path('deletePartner/<int:id>',views.deletePartner , name='deletePartner'),
    path('updatePartner/<int:id>', views.updatePartner, name='updatePartner'),
    path('updatePartner2/', views.updatePartner2, name='updatePartner2'),


#=======================================================================================Agent url
    path('createAgent/', views.createAgent, name='createAgent'), 
    path('saveAgent/', views.saveAgent, name='saveAgent'),
    path('showAgent/',views.showAgent, name='showAgent'),
    path('updateAgent/<int:id>',views.updateAgent, name='updateAgent'),
    path('save_updateAgent/',views.save_updateAgent, name='save_updateAgent'),
    path('deleteAgent/<int:id>',views.deleteAgent, name = 'deleteAgent'),
    #=======================================================================================promoter url
    path('createPromoter/', views.createPromoter, name='createPromoter'), 
    path('savePromoter/', views.savePromoter, name='savePromoter'),
    path('showPromoter/',views.showPromoter, name='showPromoter'),
    path('updatePromoter/<int:id>',views.updatePromoter, name='updatePromoter'),
    path('save_updatePromoter/',views.save_updatePromoter, name='save_updatePromoter'),
    path('deletePromoter/<int:id>',views.deletePromoter, name = 'deletePromoter'),






    #======================================================================================= urlCategory    
    path('createCategory/', views.createCategory, name='createCategory'),
    path('saveData/',views.saveData, name='saveData'),
    path('showCategory/', views.showCategory, name='showCategory'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('updateCategory/<int:id>', views.updateCategory, name='updateCategory'),
    path('update', views.update, name='update'),

#============================================================================================= urlsubCategory

    path('createSubCategory/', views.createSubCategory, name='createSubCategory'),
    path('saveDataSubCategory/',views.saveDataSubCategory,name='saveDataSubCategory'),
    path('showSubCategory/', views.showSubCategory, name='showSubCategory'),
    path('Sub_delete/<int:id>', views.Sub_delete, name='Sub_delete'),
    path('updateSubCategory/<int:id>', views.updateSubCategory, name='updateSubCategory'),
    path('Sub_update', views.Sub_update, name='Sub_update'),



##=======================================================================================Offer url
    path('createOffer/', offer_view.createOffer, name='createOffer'),
    path('showOffer/', offer_view.showOffer, name='showOffer'),
    path('saveOffer/', offer_view.saveOffer, name='saveOffer'),
    path('deleteOffer/<int:id>', offer_view.deleteOffer, name='deleteOffer'),
    path('updateOffer/<int:id>', offer_view.updateOffer, name='updateOffer'),
    path('Offer_update', offer_view.Offer_update, name='Offer_update'),

    #===============================================================================================bookingUrl
    path('createBooking/',bookingViews.createBooking, name='createBooking'),
    path('saveBooking/', bookingViews.saveBooking,  name='saveBooking'),
    path('showBooking/' , bookingViews.showBooking , name='showBooking'),
    path('deleteBooking/<int:id>', bookingViews.deleteBooking, name='deleteBooking'),
    path('updateBooking/<int:id>', bookingViews.updateBooking, name='updateBooking'),
    path('updateBooking2/', bookingViews.updateBooking2, name='updateBooking2'),
    #===============================================================================================bookingItemsUrl
    path('showBooking_items/' , bookingViews.showBooking_items , name='showBooking_items'),

    #===============================================================================================BannerUrl
    path('createBanner/',views.createBanner, name='createBanner'),
    path('saveBanner/', views.saveBanner,  name='saveBanner'),
    path('showBanner/' , views.showBanner , name='showBanner'),
    path('deleteBanner/<int:id>', views.deleteBanner, name='deleteBanner'),
    path('updateBanner/<int:id>', views.updateBanner, name='updateBanner'),
    path('saveUpdatebanner/', views.saveUpdatebanner, name='saveUpdatebanner'),

   #===============================================================================================AppConfigUrl  
     path('createAppconfig/',bookingViews.createAppconfig, name='createAppconfig'),


  #===============================================================================================RatingUrl 
     path('createRating/',Rating_views.createRating, name='createRating'),
     path('saveRating/', Rating_views.saveRating,  name='saveRating'),
     path('showRating/' , Rating_views.showRating , name='showRating'),
     path('deleteRating/<int:id>', Rating_views.deleteRating, name='deleteRating'), 


#===============================================================================================PackageUrl 


    path('CreatePackage/', views.Createpackage, name='CreatePackage'),
    path('CreatePackage-save/', views.save, name='CreatePackage-save'),
    path('showCreatePackageInfo/', views.showCreatePackageInfo, name='showCreatePackageInfo'),
    path('deletePackage/<int:id>', views.deletePackage, name='deletePackage'),
    path('updatepackage/<int:id>', views.updatePackage, name='updatepackage'),
    path('updatedPackageForm/', views.updatedPackage, name='updatedPackageForm'),

#===============================================================================================incomeHistoryUrl 

    path('incomeHistory/', views.incomeHistory, name='incomeHistory'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)