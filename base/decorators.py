from django.shortcuts import redirect

def student_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'student_id' not in request.session:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper