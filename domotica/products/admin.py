from django.contrib import admin

# Register your models here.
from .models import Product, Product_type, Provider

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
        list_display = ["name" ,"pk", "description", "price"]
        filter_horizontal = ["providers"]

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
        list_display = ["name", "phone", "web", "email"]


@admin.register(Product_type)
class ProductTypeAdmin(admin.ModelAdmin):
        list_display = ["name"]
        list_filter = ["name"]
