from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name="loginpage"),
    path('', views.home, name="home"),
    path('login/studentdash/', views.studentdashboard, name="studentdash"),
    path('login/admindash/', views.admindashboard, name="admindash"),
    # path('room/<str:pk>/', views.room, name="room"),
] 
