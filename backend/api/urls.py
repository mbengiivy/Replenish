from django.urls import path
from . import views


urlpatterns = [
path('products/', views.products_list, name='products_list'),
path('orders/', views.orders_list, name='orders_list'),
path('staff-count/', views.staff_count, name='staff_count'),
]