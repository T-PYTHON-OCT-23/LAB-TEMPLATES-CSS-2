from django.urls import path
from . import views


app_name = "main"


urlpatterns = [
    path('', views.home_views , name="home_views"),
    path('about/', views.about_views , name="about_views"),
    path('about/large/', views.large_size , name="large_size"),
    path('about/small/', views.small_size , name="small_size"),



]