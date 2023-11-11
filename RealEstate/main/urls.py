from . import views
from django.urls import path


app_name = "main"


urlpatterns = [
    path("", views.home_page_view , name="home_page_view"),
    path("/properties", views.properties_page_view, name="properties_page_view"),
]