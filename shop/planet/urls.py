from django.urls import path
from . import views

urlpatterns = [
    path("", views.menu_view, name="menu_view"),
    path("planets/", views.menu_view),
    path("trips/", views.trip_view, name="trips")
]