from django import forms

class ContactForm(forms.Form):
    from_name = forms.CharField(
        required=True,
        label='Name:',
        widget=forms.TextInput(
            attrs={'class':'contact-form-textfield', 
            'placeholder':'Enter your name...'},
        ))
        
    from_email = forms.EmailField(
        required=True,
        label='Email:', 
        widget=forms.TextInput(
            attrs={'class':'contact-form-textfield',
            'placeholder':'Enter your email...'},
        ))
        
    subject = forms.CharField(
        required=True,
        label='Subject:',
        widget=forms.TextInput(
            attrs={'class':'contact-form-textfield',
            'placeholder':'Message subject...'},
        ))
        
    message = forms.CharField(
        required=True,
        label='Message:',
        widget=forms.Textarea(
            attrs={'class':'contact-form-textfield',
            'placeholder':'Enter your message...'},
        ))