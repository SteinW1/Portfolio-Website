from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
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
                return redirect('contact-form')
            messages.success(request, f'Thank you, your message has been sent!')
            return redirect('contact-form')
        else:
            for error_message in form.messages:
                messages.error(request, '{error_message}: {form.error_messages.[error_message]}')
        print(form.errors)
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form, 'portfolio_view_name': 'contact', 'recaptcha_site_key':settings.RECAPTCHA_SITE_KEY})
