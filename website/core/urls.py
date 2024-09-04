from django.urls import path

# importing from views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("weather/", views.weather, name="weather"),
]
