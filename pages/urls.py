# not complete

from django.urls import path , re_path 
from . import views

urlpatterns = [
    # path('',views.index, name='index'),
     path('',views.index, name='index'),
     path('info/',views.info, name='info'),
     path('election/',views.election, name='election'),
     path('info/sisi',views.sisi, name='sisi'),
     path('info/hazem',views.hazem, name='hazem'),
     path('info/abd el sanad',views.abd_el_sanad, name='abd_el_sanad'),
     path('info/mohamed',views.mohamed, name='mohamed'),
    #  path('createAcc/login/',views.login, name='login'),
    # path('createAcc/login/createAcc',views.createAcc, name='login-createAcc'),
     path('createAcc/login/getPhoneNumber',views.getPhoneNumber, name='get-phonenumber'),
     path('createAcc/login/getCode/',views.getCode, name='get code'),
     path('createAcc/login/getCode/newPassword',views.newPassword, name='new-Password'),
     path('createAcc/login/getCode/newPassword/login',views.newPassword, name='new-Password'),
     path('createAcc/login/startElection/',views.startElection, name='start-Election'),
     path('createAcc/login/startElection/election/',views.election, name='startElection'),

     path('createAcc/login/startElection/election/sendMassege',views.sendMassege, name='sendMassege'),
     path('election/sendMassege',views.sendMassege, name='sendMassege'),
     path('createAcc/login/startElection/election/index',views.index, name='index'),
     path('election/index',views.index, name='index'),
  
   
     #digram url
     path('diagram/',views.DiagramView, name='diagram'),


]
