from django.urls import path

from credentials import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    # path('add/',views.addition,name='addition'),
    # path('contact/',views.contact,name='contact'),
]