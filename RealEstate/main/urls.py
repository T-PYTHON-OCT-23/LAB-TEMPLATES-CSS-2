from django.urls import path 
from . import views 
app_name  = "main"
urlpatterns = [
    path("", views.home ,name="home"),
    path("properties/", views.properties, name="properties" ),
    path("service/", views.service,name="service"),
    path("about/", views.about,name="about"),
    path('large/size',views.large_view,name="large_view"),
    path('small/size',views.small_view,name="small_view")
]
