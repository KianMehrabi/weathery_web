from django.urls import path

# importing from views
from . import views

urlpatterns = [
    path("weather/", views.WeatherApi.as_view(), name="weatherApi"),
]
