from django.contrib import admin


from .models import OrderStatus, OrderItem, Order

class OrderItemInlineAdmin(admin.StackedInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInlineAdmin]
    pass

@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    pass

