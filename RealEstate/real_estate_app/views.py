from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse



# Create your views here.
def home_page(request : HttpRequest):
    return render(request, "real_estate_app/home.html")

def about_page(request : HttpRequest):
    return render(request, "real_estate_app/about.html")

def large_font_view(requset: HttpRequest):

    response = redirect("real_estate_app:about_page")
    response.set_cookie("font", "large")

    return response


def small_font_view(requset: HttpRequest):

    response = redirect("real_estate_app:about_page")
    response.set_cookie("font", "small")

    return response