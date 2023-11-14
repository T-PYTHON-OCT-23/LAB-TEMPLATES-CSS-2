from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("about/",views.about_view,name="about_view"),
    path("large/font/",views.font_large_view,name="font_large_view"),
    path("small/font/",views.font_small_view,name="font_small_view"),
]