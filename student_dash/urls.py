from django.urls import path
from . import views

app_name = 'dash'
urlpatterns = [
    path('request/', views.inventory_request, name='inventory_request'),
    path('login/studentdash/components', views.components, name="components"),
    path('category/<str:category_key>/', views.category_items, name='category_items'),
    path('submit-request/', views.submit_request, name='submit_request'),
]