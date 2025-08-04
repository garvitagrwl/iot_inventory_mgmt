from django.contrib import  messages
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from base.decorators import student_login_required
from django.contrib.auth.hashers import make_password, check_password
from base.models import Student, Component
from student_dash.models import StudentIssueLog


@student_login_required
def inventory_request(request):
    return render(request, 'student_dash/inventory_request_view.html')

@student_login_required
def components(request):
    categories = dict(Component.CATEGORY_CHOICES)
    return render(request, 'student_dash/inventory_request_view.html', {'categories': categories})
@student_login_required
def category_items(request, category_key):
    components = Component.objects.filter(category=category_key)
    category_name = dict(Component.CATEGORY_CHOICES).get(category_key, "Unknown")
    return render(request, 'student_dash/category_items.html', {
        'components': components,
        'category_name': category_name,
    })


from django.http import JsonResponse

@student_login_required
def submit_request(request):
    if request.method == 'POST':
        component_ids = request.POST.getlist('component_ids[]')
        quantities = request.POST.getlist('quantities[]')

        if len(component_ids) != len(quantities):
            return HttpResponseBadRequest("Mismatched data")

        student = request.student

        for comp_id, qty in zip(component_ids, quantities):
            try:
                component = Component.objects.get(id=comp_id)
            except Component.DoesNotExist:
                continue

            StudentIssueLog.objects.create(
                student=student,
                component=component,
                quantity_issued=int(qty),
                status_from_teacher='Pending',
                status_from_student='Requested',  # or leave default
            )

        response = redirect('dash:components')
        response.set_cookie('clearLocalStorage', 'true')  # instruct frontend to clear
        return response
