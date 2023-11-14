from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.RealEstate_view, name="RealEstate_view"),
    path("about/", views.about_view, name="about_view"),
    path("fontsize/large/", views.large_view, name="large_view"),
    path("fontsize/small/", views.small_view, name="small_view")

]