from django.shortcuts import render
from .models import Project

def home(request):
    context = {
        'view_name': "home",
    }
    return render(request, 'portfolio/home.html', context)

def projects_list(request):
    context = {
        'view_name': "projects",
        'project': Project.objects.all(),
    }
    return render(request, 'portfolio/projects_list.html', context)

def projects(request, project_name):
    context = {
        'view_name': "projects"
    }
    return render(request, 'portfolio/projects.html', context)

def resume(request):
    context = {
        'view_name': "resume",
    }
    return render(request, 'portfolio/resume.html', context)

def contact(request):
    context = {
        'view_name': "contact",
    }
    return render(request, 'portfolio/contact.html', context)