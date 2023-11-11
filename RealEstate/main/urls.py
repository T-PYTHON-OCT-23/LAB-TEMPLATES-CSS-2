from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_page_view, name="home_page_view"),
    path("propertes/",views.propertes_page_view,name="propertes_page_view"),
    path("service/",views.service_page_view,name="service_page_view"),
    path("about/",views.about_page_view,name="about_page_view"),
    path("contacts/",views.contacts_page_view,name="contacts_page_view"),
]