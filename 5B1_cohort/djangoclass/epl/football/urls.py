from django.urls import path
from . import views

urlpatterns = [
    path("heading/", views.home_page, name = "homepage"),
    path("blogs/", views.blog_page, name = "blogpage"),
    path("kibbos/", views.kibbo_page, name = "kibbopage")
]