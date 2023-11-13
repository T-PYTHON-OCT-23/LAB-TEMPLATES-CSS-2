from django.urls import path
from .import views

app_name ='main'

urlpatterns =[
    path('',views.index, name='home'),
    path('about/',views.about,name='about'),
    path('font/large/',views.large_font,name='font_large'),
    path('font/small/',views.small_font,name='font_small')


]
