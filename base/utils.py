import random
from django.core.mail import send_mail
from django.conf import settings
from .models import StudentOTP
def generate_otp():
    return f"{random.randint(0, 999999):06}"

def create_and_send_otp(email):
    # delete old OTPs for this email
    StudentOTP.objects.filter(student_email=email).delete()
    code = generate_otp()
    otp = StudentOTP.objects.create(student_email=email, code=code)
    send_mail(
        subject="Your IoT Lab Portal OTP",
        message=f"Your code is {code}. It expires in 10 minutes.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
    )
    return otp.session_key
