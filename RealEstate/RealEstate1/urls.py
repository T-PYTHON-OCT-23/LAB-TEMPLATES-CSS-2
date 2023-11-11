from django.urls import path
from . import views


app_name = "RealEstate1"

urlpatterns = [
    path("", views.homePage, name="homePage"),
]