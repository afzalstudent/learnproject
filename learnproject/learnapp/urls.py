from xml.etree.ElementInclude import include

from django.urls import path



from django.urls import path

from learnapp import views

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('add/',views.addition,name='addition'),
    # path('contact/',views.contact,name='contact'),
]