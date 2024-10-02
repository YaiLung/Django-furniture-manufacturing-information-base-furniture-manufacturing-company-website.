from django.contrib import admin
from .models import Product, Client, Order, Warehouse, Staff

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published', 'category')
    list_filter = ('is_published', 'time_create', 'category')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'product', 'quantity', 'total_price', 'created_at')
    list_display_links = ('id',)
    list_filter = ('created_at',)
    search_fields = ('client__name', 'product__title')

class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'capacity')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'location')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'department', 'salary', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'position', 'department')
    list_filter = ('department', 'position', 'hire_date')

admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Staff, StaffAdmin)





