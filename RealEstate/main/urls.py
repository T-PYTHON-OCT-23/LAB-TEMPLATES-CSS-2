from . import views
from django.urls import path


app_name = "main"


urlpatterns = [
    path("", views.home_page_view , name="home_page_view"),
    path("properties/", views.properties_page_view, name="properties_page_view"),
    path("our/service/", views.service_page_view, name="service_page_view"),
    path("contract/", views.contract_page_view, name="contract_page_view"),
    path("about/us/", views.about_page_view, name="about_page_view"),
]