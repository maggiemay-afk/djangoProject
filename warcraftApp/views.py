from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import SurveyForm


# Create your views here.
def index(request):
    return render(request, "warcraftApp/index.html")


def about(request):
    return render(request, "warcraftApp/about.html")


def history(request):
    return render(request, "warcraftApp/history.html")


def survey(request):
    if request.method == "POST":
        form = SurveyForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        return redirect(index)

    else:
        form = SurveyForm()

    return render(request, "warcraftApp/survey.html", {"form": form})


def thanks(request):
    return render(request, "warcraftApp/thanks.html")