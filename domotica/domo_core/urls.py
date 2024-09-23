from django.urls import path

from .views import HomeView, AboutUsView, LoginView, RegisterView, ContactView, logout_view

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about_us/", AboutUsView.as_view(), name="about_us"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("contact/ccbv/", ContactView.as_view(), name="contact"),
]