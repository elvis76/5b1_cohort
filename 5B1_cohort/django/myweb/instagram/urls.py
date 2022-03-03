from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.welcome),
    path("posts/", views.post),
    path("contacts/", views.contact),
    path("aboutus/", views.about),
    path("blogs/", views.blog)
]