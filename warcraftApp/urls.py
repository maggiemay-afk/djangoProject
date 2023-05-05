from django.urls import path, include
from warcraftApp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("expansions/", views.expansions, name="expansions"),
    path("survey/", views.survey, name="survey"),
    path("thanks/", views.thanks, name="thanks")
]
