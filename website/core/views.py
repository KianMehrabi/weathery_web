from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("This is Home Page!!!")


def weather(request):
    return HttpResponse("This is the Weather Page!!!")
