from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='portfolio-home'),
    #path('projects/', views.projects, name='portfolio-projects'),
    #path('resume/', views.resume, name='portfolio-resume'),
    #path('contact/', views.contact, name='portfolio-contact'),
]
