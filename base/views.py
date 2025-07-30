from django.contrib import  messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from .models import Room
from django.http import HttpResponse

# rooms = [
#     {'id': 1, 'name': 'Room 1'},
#     {'id': 2, 'name': 'Room 2'},
#     {'id': 3, 'name': 'Room 3'},
# ]

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

def home(request):
    # rooms = Room.objects.all()
    # context = {'rooms': rooms}
    return render(request, 'base/home.html')
                  # , context)

# def room(request, pk):
#     room = Room.objects.get(id=pk)
#     context = {'rooms': room}
#     return render(request, 'base/room.html', context)

def studentdashboard(request):
    if request.method == 'POST':
        return render(request,'base/studentdashboard.html')
    return HttpResponse("not a post emthi")


def admindashboard(request):
    if request.method == 'POST':
        return render(request, 'base/admin-dashboard.html')
    return HttpResponse("not a post emthi from admin")