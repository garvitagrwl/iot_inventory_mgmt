from django.contrib import  messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from base.decorators import student_login_required
from django.contrib.auth.hashers import make_password, check_password


@student_login_required
def inventory_request(request):
    return render(request, 'inventory_request_view.html')
