from django.shortcuts import render

# Create your views here.
def newreg(request):
    return render(request,"registration.html")