from django.contrib import admin
from .models import Category, Product, Subscription

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'is_active', 'is_featured']
    list_filter = ['category', 'is_active', 'is_featured', 'is_deal']
    search_fields = ['name', 'category__name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'frequency', 'start_date', 'is_active']
    list_filter = ['frequency', 'is_active']
    search_fields = ['user__username', 'product__name']
