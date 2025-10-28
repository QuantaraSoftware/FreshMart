from django.contrib import admin
from .models import Order, OrderItem, PromoCode

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user', 'status', 'total', 'payment_status', 'created_at']
    search_fields = ['order_id', 'user__username', 'delivery_name']
    list_filter = ['status', 'payment_status']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product_name', 'product_price', 'quantity', 'subtotal']

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount_type', 'discount_value', 'is_active']
    search_fields = ['code']
