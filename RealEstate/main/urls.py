from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.RealEstate_view, name="RealEstate_view")

]