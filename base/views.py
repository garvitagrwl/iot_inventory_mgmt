from .models import Component
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': 'Room 1'},
    {'id': 2, 'name': 'Room 2'},
    {'id': 3, 'name': 'Room 3'},
]
def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
            return render(request, 'base/login_register.html', {})
        user = authenticate(request, username=user_obj, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Wrong User ID and Password.")
    context = {}
    return render(request, 'base/login_register.html', context)

def home(request):

    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'rooms': room}
    return render(request, 'base/room.html', context)