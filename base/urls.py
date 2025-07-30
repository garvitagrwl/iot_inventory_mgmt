from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
path('student_reg/', views.student_reg, name="student_reg"),
    path('', views.home, name="home"),
    # path('room/<str:pk>/', views.room, name="room"),
    path('login/studentdash/', views.studentdashboard, name="studentdash"),
    path('login/admindash/', views.admindashboard, name="admindash"),
    # path('room/<str:pk>/', views.room, name="room"),
] 
