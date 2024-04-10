from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from app1.forms import UserForm
# from app2.forms import EmployeeForm
from .models import user
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'homepage.html')

def AdvisoryPage(request):
    return render (request,'advisorypage.html')   

def DeliveryPage(request):
    return render (request,'deliverypage.html') 

@login_required(login_url='login')
def ProductPage(request):
    return render (request,'products.html')    

@login_required(login_url='login')
def AboutPage(request):
    return render (request,'about.html')   

def LandingPage(request):
    return render (request,'landingpage.html') 


def CompanyPage(request):
    return render (request,'company.html') 

def Company1Page(request):
    return render (request,'company1.html')     

def Company2Page(request):
    return render (request,'company2.html')      

@login_required(login_url='login')
def ContactPage(request):
    user_form=UserForm()
    context={
        'form':user_form
    }
    return render (request,'contact.html',context) 

@login_required(login_url='login')
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Password does not match")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        


    return render (request,'signup.html')

def LoginPage(request):   
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        print(username,pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect")



    return render (request,'login.html') 


def LogoutPage(request):
    logout(request)
    return redirect('login')    

def save_form(request):
    if request.method=="POST":
        user_name=request.POST['user_name']
        user_email=request.POST['user_email']
        user_phone=request.POST['user_phone']
        my_model=user(usr_name=user_name,usr_email=user_email,usr_phone=user_phone)
        my_model.save()
    return HttpResponse("Your request has been received. We will respond to you as soon as possible.")


def vendorlogin1(request):
    return render (request,'vendorlogin.html')

def vendorsignup1(request):
    return render (request,'vendorsignup.html') 



def vendorsignup1(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Password does not match")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('vendorlogin1')
        


    return render (request,'vendorsignup1.html')

def vendorlogin1(request):   
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        print(username,pass1)
        if user is not None:
            login(request,user)
            return redirect('appindex')
        else:
            return HttpResponse ("Username or Password is incorrect")



    return render (request,'vendorlogin1.html')     

# def VendorBasePage(request):
#     return render (request,'vendorbase.html') 

# def VendorIndexPage(request):
#     return render (request,'vendorindex.html')

# def VendorUpdatePage(request):
#     return render (request,'vendorupdate.html')           