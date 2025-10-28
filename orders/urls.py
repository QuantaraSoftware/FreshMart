from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('confirmation/<str:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('my_orders/', views.order_list, name='order_list'),
]
