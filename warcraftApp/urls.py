from django.urls import path, include
from warcraftApp import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("history/", views.history, name="history")

]
