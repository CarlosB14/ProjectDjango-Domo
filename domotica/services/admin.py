from django.contrib import admin
from .models import Service, Services


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
        list_display = ["title", "pk", "description"]

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
        list_display = ["title", "pk", "show_home", "description"]