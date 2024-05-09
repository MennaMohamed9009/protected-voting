# not complete

from django.urls import path , re_path 
from . import views

urlpatterns = [
    # path('',views.index, name='index'),
     path('createAcc/',views.createAcc, name='create-account'),
     path('login/',views.login_view, name='login'),
     path('login/getCode/newPassword/getCode/getPhoneNumber',views.getPhoneNumber, name='get-phonenumber'),
     path('login/getCode/newPassword/getCode/getCode',views.getCode, name='get code'),
     path('login/getCode/newPassword/getCode/newPassword',views.newPassword, name='new-Password'),
     path('login/getCode/newPassword/getCode/newPassword/login',views.login_view, name='login'),
     path('login/getCode/newPassword/getCode/login',views.login_view, name='login'),
]
