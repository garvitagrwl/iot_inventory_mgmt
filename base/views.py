from django.contrib import  messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .decorators import student_login_required

from .models import Student
def loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(college_email=email)
        except Student.DoesNotExist:
            messages.error(request, "Student does not exist.")
            return render(request, 'base/login_register.html')

        if student.password == password:
            request.session['student_id'] = student.id  # custom session
            return redirect('studentdash')
        else:
            messages.error(request, "Invalid email or password.")
    context = {}
    return render(request, 'base/login_register.html',context)

def home(request):
    return render(request, 'base/home.html')
def student_reg(request):
    if request.method == 'POST':
        email = request.POST.get('College_Email')
        password = request.POST.get('password')
        student_name = request.POST.get('Full_Name')
        roll_no = request.POST.get('Roll_Number')
        contact_number = request.POST.get('Contact_Number')
        # print(email,roll_no)

        student = Student(
            full_name = student_name,
            roll_number=roll_no,
            college_email=email,
            contact_number=contact_number,
           )
        student.set_password(password) 
        student.save()
    context = {}
    return render(request, 'base/login_register.html', context)
# def studentdashboard(request):
#     if request.method == 'POST':
#         return render(request,'base/studentdashboard.html')
#     return HttpResponse("not a post emthi")
@student_login_required
def studentdashboard(request):
    return render(request, 'base/studentdashboard.html')
def admindashboard(request):
    if request.method == 'POST':
        return render(request, 'base/admin-dashboard.html')
    return HttpResponse("not a post emthi from admin")
def student_logout(request):
    request.session.flush()
    return redirect('login')
