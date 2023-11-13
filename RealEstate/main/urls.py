from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path("", views.home_views, name="home_views"),
    path('about/', views.about_viwes, name="about_viwes"),
    path('zoomout/', views.zoom_out, name="zoom_out"),
    path('zoomin/', views.zoom_in, name="zoom_in")
]