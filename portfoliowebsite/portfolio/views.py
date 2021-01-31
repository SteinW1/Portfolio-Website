from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView
from .models import Project
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

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

def contact(request):
    if request.method =="POST":
        print('the request was post')
        form = ContactForm(request.POST)
        if form.is_valid():
            from_name = form.cleaned_data['from_name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            contact_message = form.cleaned_data['contact_message']
            try:
                send_mail(subject, contact_message, from_email, ['admin@example.com'])
            except BadHeaderError:
                messages.error(request, f'Invalid header found.')
                return redirect('portfolio-contact')
            messages.success(request, f'Thank you, your message has been sent!')
            return redirect('portfolio-contact')
        else:
            for error_message in form.messages:
                messages.error(request, '{error_message}: {form.error_messages.[error_message]}')
        print(form.errors)
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form, 'portfolio_view_name': "contact"})

class ProjectDetailView(DetailView):
    model = Project