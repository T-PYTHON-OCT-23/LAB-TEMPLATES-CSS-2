from django.urls import path
from . import views
app_name = "real_estate_app"



urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('/about', views.about_page, name="about_page"),
    path('font/large/', views.large_font_view, name="large_font_view"),
    path('font/small/',views.small_font_view, name="small_font_view")
]