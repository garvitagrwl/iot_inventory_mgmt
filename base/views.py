from django.contrib import  messages
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .decorators import student_login_required
from django.contrib.auth.hashers import make_password, check_password
from .models import Student , Component
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, StudentOTP
from .utils import create_and_send_otp, generate_otp
from .forms import EmailForm, OTPForm, RegistrationForm
from django.utils import timezone


def loginpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(college_email=email)
        except Student.DoesNotExist:
            messages.error(request, "Student does not exist.")
            return render(request, 'base/login_register.html')

        if check_password(password, student.password):
            request.session['student_id'] = student.id  # custom session
            return redirect('studentdash')
            # return render(request,'base/studentdashboard.html',{'student':student})
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, 'base/login_register.html', {'step': 'student'})

def home(request):
    return render(request, 'base/home.html')




def verify_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Student.objects.filter(college_email=email).exists():
                messages.error(request, "Email already registered.")
            else:
                key = create_and_send_otp(email)
                request.session['otp_email'] = email
                request.session['otp_session_key'] = str(key)
                return redirect('enter_otp')
    else:
        form = EmailForm()
    return render(request, 'base/login_register.html', {'step': 'email', 'form': form})

def enter_otp(request):
    key = request.session.get('otp_session_key')
    email = request.session.get('otp_email')
    if not key or not email:
        return redirect('verify_email')
    try:
        otp_rec = StudentOTP.objects.get(session_key=key, student_email=email)
    except StudentOTP.DoesNotExist:
        messages.error(request, "Invalid session. Start over.")
        return redirect('verify_email')

    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            if otp_rec.is_expired():
                otp_rec.delete()
                messages.error(request, "OTP expired.")
                return redirect('verify_email')

            if form.cleaned_data['code'] == otp_rec.code:
                otp_rec.delete()
                request.session['verified_email'] = email
                return redirect('complete_registration')
            otp_rec.attempts += 1
            otp_rec.save()
            left = 3 - otp_rec.attempts
            if left <= 0:
                otp_rec.delete()
                messages.error(request, "Too many tries.")
                return redirect('verify_email')
            messages.error(request, f"Wrong OTP. {left} tries left.")
    else:
        form = OTPForm()
    return render(request, 'base/login_register.html', {'step': 'otp', 'form': form})

def resend_otp(request):
    key = request.session.get('otp_session_key')
    email = request.session.get('otp_email')
    if not key or not email:
        return redirect('verify_email')
    otp_rec = StudentOTP.objects.filter(session_key=key, student_email=email).first()
    if not otp_rec:
        return redirect('verify_email')
    if otp_rec.resent_count >= 3:
        otp_rec.delete()
        messages.error(request, "Resend limit reached.")
        return redirect('verify_email')
    otp_rec.code = generate_otp()
    otp_rec.created_at = timezone.now()
    otp_rec.resent_count += 1
    otp_rec.attempts = 0
    otp_rec.save()
    send_mail(
        subject="Your IoT Lab OTP (Resent)",
        message=f"Your new OTP is {otp_rec.code}.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
    )
    messages.success(request, "OTP resent.")
    return redirect('enter_otp')

def complete_registration(request):
    email = request.session.get('verified_email')
    if not email:
        return redirect('verify_email')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            roll_number = form.cleaned_data['roll_number']
            if Student.objects.filter(roll_number=roll_number).exists():
                messages.error(request, "Roll number already registered.")
            else:
                student = Student(
                    college_email=email,
                    full_name=form.cleaned_data['full_name'],
                    roll_number=roll_number,
                    contact_number=form.cleaned_data['contact_number'],
                )
                student.set_password(form.cleaned_data['password'])
                student.save()
                del request.session['verified_email']
                messages.success(request, "Registration complete.")
                return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'base/login_register.html', {'step': 'register', 'form': form, 'email': email})




@student_login_required
def studentdashboard(request):
    # student = request.student   # <-- this is set by your custom decorator
    student_id = request.session.get("student_id")
    if not student_id:
        return redirect("login")  # if not logged in, send back to login

    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return redirect("login")
    return render(request, 'base/studentdashboard.html', {"student": student})



def admindashboard(request):
#     if request.method == 'POST':
        return render(request, 'base/admin-dashboard.html')
#     return HttpResponse("not a post emthi from admin")


def student_logout(request):
    request.session.flush()
    return redirect('login')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def faculty_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if not username or not password:
            messages.error(request, "Please fill in both fields.")
            return render(request, 'base/login_register.html')
            
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:  
            login(request, user)
            return redirect('dash:admindash')  
        else:
            messages.error(request, "Invalid credentials or not authorized.")
            return render(request, 'base/login_register.html')
    
    return render(request, 'base/login_register.html')

