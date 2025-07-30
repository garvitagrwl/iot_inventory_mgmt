from django.contrib import  messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Student
from django.http import HttpResponse


def loginpage(request):
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     return HttpResponse(f"{email} {password}")

        # try:
        #     user_obj = User.objects.get(email=email)
        # except User.DoesNotExist:
        #     messages.error(request, "User does not exist.")
        #     return render(request, 'base/login_register.html', {})
        # user = authenticate(request, username=user_obj, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('home')
        # else:
        #     messages.error(request, "Wrong User ID and Password.")
    # context = {}
    return render(request, 'base/login_register.html')
                  # , context)

def student_reg(request):
    if request.method == 'POST':
        email = request.POST.get('College_Email')
        password = request.POST.get('password')
        student_name = request.POST.get('Full_Name')
        roll_no = request.POST.get('Roll_Number')
        contact_number = request.POST.get('Contact_Number')
        # print(email,roll_no)

        save_item = Student(full_name = student_name,roll_number=roll_no,college_email=email,contact_number=contact_number,password=password)
        save_item.save()
    context = {}
    return render(request, 'base/login_register.html', context)


def home(request):
    # rooms = Room.objects.all()
    # context = {'rooms': rooms}
    return render(request, 'base/home.html')
                  # , context)


def studentdashboard(request):
    if request.method == 'POST':
        return render(request,'base/studentdashboard.html')
    return HttpResponse("not a post emthi")


def admindashboard(request):
    if request.method == 'POST':
        return render(request, 'base/admin-dashboard.html')
    return HttpResponse("not a post emthi from admin")