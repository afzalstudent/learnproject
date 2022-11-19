from django.urls import path

from newapp import views

urlpatterns = [
    path('newreg/',views.newreg,name='newreg'),

]