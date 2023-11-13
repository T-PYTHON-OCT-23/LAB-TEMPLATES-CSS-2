from django.urls import path
from . import views

app_name = "Home"
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("large/size/", views.large_size, name="large_size"),
    path("small/size/", views.small_size, name="small_size"),
]
