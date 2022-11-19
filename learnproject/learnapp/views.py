from urllib import request

from django.shortcuts import render
from django.http import HttpResponse
from .models import place
from .models import team


# Create your views here.


def demo(request):
    obj = place.objects.all()
    tms = team.objects.all()
    return render(request, "index.html", {'result': obj, 'items': tms})

# def addition(request):
#     num1 = int(request.GET["number 1"])
#     num2 = int(request.GET["number 2"])
#     res = num1 + num2
#     return render(request, "about.html", {'result':res})
#
#
# def contact(request):
#     return HttpResponse('this is contact')
def register():
         return render(request,"registration.html")
