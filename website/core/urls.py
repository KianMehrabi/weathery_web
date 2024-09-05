from django.urls import path

# importing from views
from . import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("weather/", views.WeatherPage.as_view(), name="weather"),
]
