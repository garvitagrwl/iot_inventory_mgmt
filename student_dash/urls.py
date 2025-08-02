from django.urls import path
from . import views

app_name = 'dash'
urlpatterns = [
    path('request/', views.inventory_request, name='inventory_request'),
    
]