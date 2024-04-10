from django.shortcuts import render

# Create your views here.
def vendorlogin(request):
    return render (request,'vendorlogin.html')

def vendorsignup(request):
    return render (request,'vendorsignup.html')  