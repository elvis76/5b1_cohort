from django.urls import path
from . import views

urlpatterns = [
    path("heading/", views.home_page, name = "homepage"),
    path("aboutus/", views.about_page, name = "aboutpage"),
]
