from django.urls import path
from . import views

app_name = 'dash'
urlpatterns = [
    path('request/', views.inventory_request, name='inventory_request'),
    path('login/studentdash/components', views.components, name="components"),
    path('category/<str:category_key>/', views.category_items, name='category_items'),
    path('submit-request/', views.submit_request, name='submit_request'),
    path('admindash/', views.admindashboard, name="admindash"),
    path("admindash/approved/",views.approved_requests,name="approved_requests"),
    path("admindash/rejected/",views.rejected_requests,name="rejected_requests"),
    path('update-status/', views.update_status, name='update_status'),
    path('admindash/inventory/', views.change_inventory, name='inventory_page'),
    path('admindash/inventory/category/<str:category_key>/', views.inv_items, name='inv_items'),
]