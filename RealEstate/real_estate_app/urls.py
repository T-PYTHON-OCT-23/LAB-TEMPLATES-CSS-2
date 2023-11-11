from django.urls import path
from . import views
app_name = "real_estate_app"



urlpatterns = [
    path('', views.home_page, name="home_page"),

]