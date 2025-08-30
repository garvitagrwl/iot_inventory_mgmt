# from django.shortcuts import redirect
# from base.models import Student

# def student_login_required(view_func):
#     def wrapper(request, *args, **kwargs):
#         student_id = request.session.get('student_id')
#         if not student_id:
#             return redirect('login')

#         try:
#             request.student = Student.objects.get(id=student_id)
#         except Student.DoesNotExist:
#             return redirect('login')

#         return view_func(request, *args, **kwargs)
#     return wrapper
from functools import wraps
from django.shortcuts import redirect
from base.models import Student

def student_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        student_id = request.session.get('student_id')
        if not student_id:
            return redirect('login')  # make sure "login" is a named URL

        try:
            request.student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            # clear bad session
            request.session.flush()
            return redirect('login')

        return view_func(request, *args, **kwargs)
    return wrapper