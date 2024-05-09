# not complete

from django.urls import path  
from . import views

urlpatterns = [
        path('classify/', views.find_user_view, name='classify'),
        path('detectFace/', views.face_view, name='face'),
        path('recognitionFaild/',views.recognition_Faild, name='faild-recognition'),

     ]