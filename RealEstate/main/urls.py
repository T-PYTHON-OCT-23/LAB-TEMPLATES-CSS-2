from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
     path("main/", views.main_view, name="main_view"),
     path("", views.home_view, name="home_view"),
     path("properites/", views.properites_view, name="properites_view"),
     path("services/", views.services_view, name="services_view"),
     path("about/", views.about_view, name="about_view"),
     path("contact/", views.contact_view, name="contact_view"),
     path("size/small/", views.small_view, name="small_view"),
     path("size/large/", views.large_view , name="large_view"),
]