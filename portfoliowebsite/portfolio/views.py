from django.shortcuts import render
from django.views.generic import DetailView
from .models import Project

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .forms import ContactForm

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

def resume(request):
    context = {
        'view_name': "resume",
    }
    return render(request, 'portfolio/resume.html', context)

def contact(request):
    if request.method =="POST":
        print('the request was post')
        form = ContactForm(request.POST)
        if form.is_valid():
            from_name = form.cleaned_data['from_name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('portfolio-contact-success')
        print(form.errors)
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})

def contact_success(request):
    return HttpResponse('Success! Thank you for your message.')

class ProjectDetailView(DetailView):
    model = Project