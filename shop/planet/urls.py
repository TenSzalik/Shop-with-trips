from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu_view, name="menu_view"),
    path("planets/", views.menu_view),
    path("trips/", views.trip_view, name="trips"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]