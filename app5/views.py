from django.shortcuts import render,redirect
from app5.models import Employees

# Create your views here.
def appindex(request):
    emp = Employees.objects.all()

    context = {
        'emp':emp,
    }
    return render (request,'appindex.html',context) 


def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        emp = Employees(
            name = name,
            email = email,
            address = address,
            phone = phone 
        )
        emp.save()
        return redirect('appindex')
    return render (request,'appindex.html')   

def edit(request):
    emp = Employees.objects.all()

    context = {
        'emp':emp,
    }

    return render (request,'appindex.html',context)      


def update(request,id):   
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

        emp = Employees(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone 
        )
        emp.save()
        return redirect('appindex')

    return render (request,'appindex.html') 

def delete(request,id):
    emp = Employees.objects.filter(id = id)
    emp.delete()

    context = {
        'emp':emp,
    }

    return redirect('appindex')

# def VendorSignupPage(request):
#     if request.method=='POST':
#         uname=request.POST.get('username')
#         email=request.POST.get('email')
#         pass1=request.POST.get('password1')
#         pass2=request.POST.get('password2')

#         if pass1!=pass2:
#             return HttpResponse("Password does not match")
#         else:
#             my_user=User.objects.create_user(uname,email,pass1)
#             my_user.save()
#             return redirect('login')
        


#     return render (request,'signup.html')

# def VendorLoginPage(request):   
#     if request.method=='POST':
#         username=request.POST.get('username')
#         pass1=request.POST.get('pass')
#         user=authenticate(request,username=username,password=pass1)
#         print(username,pass1)
#         if user is not None:
#             login(request,user)
#             return redirect('appindex')
#         else:
#             return HttpResponse ("Username or Password is incorrect")



#     return render (request,'login.html')     
