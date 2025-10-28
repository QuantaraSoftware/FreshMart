from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('pay/<str:order_id>/', views.payment_page, name='payment_page'),
]
