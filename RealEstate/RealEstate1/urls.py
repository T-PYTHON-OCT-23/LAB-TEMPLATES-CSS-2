from django.urls import path
from . import views


app_name = "RealEstate1"

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path("about/", views.aboutPage, name="about"),
    path("size/large/", views.large_size_view, name="large_size_view"),
    path("size/small/", views.small_size_view, name="small_size_view"),
     
]