from django.urls import path
from . import views

app_name = "main1"


urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("another", views.another_view, name="another_view"),
    path("mode/small/", views.small_mode_view, name="small_mode_view"),
    path("mode/big/", views.big_mode_view, name="big_mode_view"),
    
]