from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
 # post views
    path('', views.post_list, name='post_list'),
    path('posts/<int:year>/<int:month>/<int:day>/<slug:slug>/',views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('adds/', views.post_add, name='post_add')
]


# urlpatterns = [
#     # path("heading/", views.home_page, name = "homepage"),
#     # path("aboutus/", views.about_page, name = "aboutpage"),
#     # path("about/student/<int:student_id>", views.student_detail, name = "student_detail")
# ]