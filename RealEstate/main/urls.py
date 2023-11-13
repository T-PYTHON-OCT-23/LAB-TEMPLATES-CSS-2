from django.urls import path
from . import views
app_name = "main"
urlpatterns = [path("", views.home_page, name="home_page"),
               path('about',views.about_page,name='about_page'),
               path('large/size',views.large_size_view,name='large_size_view'),
               path('small/size',views.small_size_view,name='small_size_view')
               ]
