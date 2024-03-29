from django.urls import path
from .views import ProjectDetailView
from . import views

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('projects/', views.projects_list, name='portfolio-projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('resume/', views.resume, name='portfolio-resume'),
]