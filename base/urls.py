from django.urls import path, include
from . import views
from django.urls import path
from .views import verify_email, enter_otp, resend_otp, complete_registration

urlpatterns = [
    path('login/', views.loginpage, name="login"),
    path('', views.home, name="home"),
    path('login/studentdash/', views.studentdashboard, name="studentdash"),
    path('login/admindash/', views.faculty_login_view, name="admindash2"),
    
    path('logout/', views.student_logout, name='logout'),
    path('student_dash/', include(('student_dash.urls', 'dash'), namespace='dash')),
    path('verify-email/', verify_email, name='verify_email'),
    path('enter-otp/',    enter_otp,    name='enter_otp'),
    path('resend-otp/',   resend_otp,   name='resend_otp'),
    path('register/',     complete_registration, name='complete_registration')
    
   
] 
