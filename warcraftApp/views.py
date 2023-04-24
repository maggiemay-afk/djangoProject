from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "warcraftApp/index.html")
    # return HttpResponse("Hello World. You're at the Warcraft index")


def about(request):
    return HttpResponse("You're at the about page")


def history(request):
    return render(request, "warcraftApp/history.html")
    # return HttpResponse("you're at the history page")
