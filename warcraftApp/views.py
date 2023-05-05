from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import SurveyModel


# Create your views here.
def index(request):
    return render(request, "warcraftApp/index.html")


def about(request):
    return render(request, "warcraftApp/about.html")


def expansions(request):
    return render(request, "warcraftApp/expansions.html")


def survey(request):
    if request.method == "POST":
        form = SurveyForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        return redirect(thanks)

    else:
        form = SurveyForm()

    return render(request, "warcraftApp/survey.html", {"form": form})


def thanks(request):
    response = SurveyModel.objects.all()
    return render(request, "warcraftApp/thanks.html", {"response": response})