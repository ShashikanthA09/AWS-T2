"""
URL configuration for registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views as app1_views
from app2 import views as app2_views
from app3 import views as app3_views
from app4 import views as app4_views
from app5 import views as app5_views
from app6 import views as app6_views
from app7 import views as app7_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',app1_views.SignupPage,name='signup'),
    path('login/',app1_views.LoginPage,name='login'),
    path('home/',app1_views.HomePage,name='home'),
    path('logout/',app1_views.LogoutPage,name='logout'),
    path('products/',app1_views.ProductPage,name='products'),
    path('advisory/',app1_views.AdvisoryPage,name='advisory'),
    path('delivery/',app1_views.DeliveryPage,name='delivery'),
    path('about/',app1_views.AboutPage,name='about'),
    path('',app1_views.LandingPage,name='landing'),
    path('contact/',app1_views.ContactPage,name='contact'),
    path('saveform/',app1_views.save_form,name='saveform'),
    path('vendorbase/',app3_views.VendorBasePage,name='vendorbase'),
    path('vendorindex/',app3_views.VendorIndexPage,name='vendorindex'),
    path('vendorupdate/',app3_views.VendorUpdatePage,name='vendorupdate'),
    path('company/',app1_views.CompanyPage,name='company'),
    path('company1/',app1_views.Company1Page,name='company1'),
    path('company2/',app1_views.Company2Page,name='company2'),
    path('index/',app4_views.index,name='index'),
    path('nav/',app4_views.nav,name='nav'),
    path('base/',app4_views.base,name='base'),
    path('appindex/',app5_views.appindex,name='appindex'),
    path('add/',app5_views.add,name='add'),
    path('edit/',app5_views.edit,name='edit'),
    path('update/<str:id>',app5_views.update,name='update'),
    path('delete/<str:id>',app5_views.delete,name='delete'),
    path('vendorsignup/',app6_views.vendorsignup,name='vendorsignup'),
    path('vendorlogin/',app6_views.vendorlogin,name='vendorlogin'),
    path('vendorsignup1/',app1_views.vendorsignup1,name='vendorsignup1'),
    path('vendorlogin1/',app1_views.vendorlogin1,name='vendorlogin1'),
    
    

]
