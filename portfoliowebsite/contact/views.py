from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from .forms import ContactForm
import requests # import requests module for easyier http for google recaptcha API

def contact(request):
    
    context = {
            'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY,
        }
        
    if request.method =="POST":
        form = ContactForm(request.POST)
        context['form'] = form # add form to context dictionary after it is declared

        if form.is_valid():
            
            reCAPTCHA_validation_result = validateRecaptcha(request)
            
            if reCAPTCHA_validation_result['success']:
                from_name = form.cleaned_data['from_name']
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                contact_message = form.cleaned_data['contact_message']
                
                try:
                    send_mail(subject, contact_message, from_email, ['admin@williamstein.com'])
                except BadHeaderError:
                    messages.error(request, f'Invalid header found.')
                    return redirect('contact-form')
                
                messages.success(request, f'Thank you, your message has been sent!')
                return redirect('contact-form')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                
        else:
            for error_message in form.errors:
                messages.error(request, f'{form.errors[error_message]}')
                
    else:
        form = ContactForm()
        context['form'] = form # add form to context dictionary after it is declared
    return render(request, 'contact/contact.html', context)
    

def validateRecaptcha(request):
    ''' 
    Function for validating a user with google's reCAPTCHA.
    
    Args:
        request: http request
    Returns:
        validated recaptcha result in format {'success': bool, 'challenge_ts': str, 'hostname': str, 'score': int 'action': str}
    '''
    recaptcha_response = request.POST.get('g-recaptcha-response')
    
    data = {
        'secret': settings.RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response,
        }
    
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    reCAPTCHA_result = r.json()
    
    return reCAPTCHA_result