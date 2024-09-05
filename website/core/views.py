from django.views.generic import TemplateView , View
from django.shortcuts import redirect , render
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
class HomePage(TemplateView):
    
    # this is the html ( css and javascript ) that its going to load
    template_name = "pages/home.html"


class WeatherPage(View):
    
    # this is the html ( css and javascript ) that its going to load
    template_name = "pages/weather.html"
    
    # if the method send to this url is get
    def get(self , request):
        
        # rendering a html file with no context processor attach to it ( empty or if you are in python {} ( a unit in C and Rust ) ).
        return render(request , self.template_name , context={})
    
    # if the method send to this url is post
    def post(self , request):
        
        # how many hours i want my data cache stay in ( redis )
        # i set it to 24 but you can change it .
        hours = 24

        # we calculate hours to seconds becouse cache.set() as the 3th arg gets seconds and not hours
        hours_to_seconds = 60 * 60 * (hours)

        if cache.get("data") != None:
            # get the data out of cache
            # "data" is the name than we set in line 45 of this file
            data = cache.get("data")
            
            """
                if you are making any changes in any place other than here you
                should delete the cache one time like this:
                
                # this deletes the data in the cache
                cache.delete("data")
            """
            
            # rendering html with data as the context processor
            return render(request , self.template_name , context={"data":data})
        else:
            # and its going to get the next 15 days
            # getting the data out of the weather api
            # documentation of weather API = "https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/"
            url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/London,UK?unitGroup=metric&key={SECRET_KEY}&include=days&elements=tempmax,tempmin&options=nonulls,noheaders"

            # using the response from the url we obtained! 
            response = requests.get(url)

            # making the ( its not valid json ) json from response itself
            data = response.json()

            # cache in ( the redis )
            cache.set("data", data, hours_to_seconds)

            # make a simple ( data ) HttpResponse
            return redirect('weather')
