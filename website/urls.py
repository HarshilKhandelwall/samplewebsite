from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('services.html', views.services, name="services"),
    path('about.html', views.about, name="about"),
    path('blog.html', views.blog, name="blog"),
    path('contact.html', views.contact, name="contact"),
    path('single.html', views.single, name="single"),
    path('portfolio.html', views.portfolio, name="portfolio"),
    path('single-portfolio.html', views.single_portfolio, name="single-portfolio"),
]
