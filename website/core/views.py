from django.views.generic import TemplateView
from django.shortcuts import render

# importing request
import requests

# importing json for (valid) json trasformasion of cache data
import json

# importing the website url
from website.settings import WEBSITE_BASE_URL

# the HomePage(TemplateView) only wants template_name and its going to set it as TemplateView
class HomePage(TemplateView):
    
    # this is the html ( css and javascript ) that its going to load 
    template_name = "pages/home.html"