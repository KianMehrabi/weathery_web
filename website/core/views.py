from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.cache import cache
import requests

# importing environ
import environ

# the url that the api offers
# the first time line is the starting point
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# importing SECRET_KEY
SECRET_KEY = env('SECRET_KEY')

# Create your views here.
def home(request):
    return HttpResponse("This is Home Page!!!")


def weather(request):
    # how many hours i want my data cache stay in ( redis )
    # i set it to 12 but you can change it .
    hours = 12

    # we calculate hours to seconds becouse cache.set() as the 3th arg gets seconds and not hours
    hours_to_seconds = 60 * 60 * (hours)

    if cache.get("data") != None:
        # get the data out of cache
        # "data" is the name than we set in line 45 of this file
        data = cache.get("data")
        
        """
            if you are making any changes in any place other than here you
            should delete the cache one of the ways is:
            
            # this deletes the data in the cache
            cache.delete("data")
        """
        
        # make a simple ( data ) HttpResponse
        return HttpResponse(f"the data is: { str(data) }")
    else:
        # and its going to get the next 15 days
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/London,UK?key={SECRET_KEY}&include=days&elements=tempmax,tempmin&options=nonulls,noheaders"

        # getting the data out of the weather api
        # documentation of weather API = "https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/"
        response = requests.get(url)

        # making the not valid json from response itself
        data = response.json()

        # cache it in ( the redis )
        cache.set("data", data, hours_to_seconds)

        # make a simple ( data ) HttpResponse
        return redirect('weather')
