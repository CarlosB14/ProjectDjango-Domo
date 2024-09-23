from django.urls import path

from .views import services_list, services_plan

app_name = "services"

urlpatterns = [
    path("", services_list, name="services_list"),
    path("<int:id>/", services_plan, name="services_plan"),
]