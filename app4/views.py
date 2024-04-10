from django.shortcuts import render
from .models import Data
from django.db.models import Q

# Create your views here.
def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(company_name__icontains=q) | Q(software_name__icontains=q))
        data = Data.objects.filter(multiple_q)
    else:
        data = Data.objects.all()
    context = {
        'data': data
    }
    return render(request, 'index.html', context)

def nav(request):
    return render (request,'nav.html')    


def base(request):
    return render (request,'base.html')    