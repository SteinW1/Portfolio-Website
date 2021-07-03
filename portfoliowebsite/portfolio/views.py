from django.shortcuts import render
from django.views.generic import DetailView
from .models import Project

def home(request):
    context = {
        'portfolio_view_name': "home",
    }
    return render(request, 'portfolio/home.html', context)

def projects_list(request):
    context = {
        'portfolio_view_name': "projects",
        'project': Project.objects.all(),
    }
    return render(request, 'portfolio/projects_list.html', context)

def resume(request):
    context = {
        'portfolio_view_name': "resume",
    }
    return render(request, 'portfolio/resume.html', context)

class ProjectDetailView(DetailView):
    model = Project
