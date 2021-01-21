from django.shortcuts import render

def home(request):
    context = {
        'view_name': "home",
    }
    return render(request, 'portfolio/home.html', context)

def projects(request):
    context = {
        'view_name': "projects",
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