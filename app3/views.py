from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.
def VendorBasePage(request):
    
    return render (request,'vendorbase.html') 

def VendorIndexPage(request):
    if request.method=="POST":
        user_name=request.POST['user_name']
        user_email=request.POST['user_email']
        user_phone=request.POST['user_phone']
        my_model=user(usr_name=user_name,usr_email=user_email,usr_phone=user_phone)
        my_model.save()
    
    return render (request,'vendorindex.html')

def VendorUpdatePage(request):
    return render (request,'vendorupdate.html')