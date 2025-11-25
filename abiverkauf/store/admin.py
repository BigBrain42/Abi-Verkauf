from django.contrib import admin
from .models import Product, Order, OrderItem, Notification

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'price', 'available')
    list_filter = ('seller',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'is_delivery', 'delivery_room', 'created_at')
    list_filter = ('status', 'is_delivery')
    inlines = [OrderItemInline]

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'read')
