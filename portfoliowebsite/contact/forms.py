from django import forms

class ContactForm(forms.Form):
    from_name = forms.CharField(
        required=True,
        label='Name:',
        widget=forms.TextInput(
            attrs={'class':'contact-form-textfield'}
        ))
        
    from_email = forms.EmailField(
        required=True,
        label='Email:', 
        widget=forms.TextInput(
            attrs={'class':'contact-form-textfield'})
        )
        
    subject = forms.CharField(
        required=True,
        label='Subject:',
        widget=forms.TextInput(
            attrs={'class':'contact-form-textfield'})
        )
        
    contact_message = forms.CharField(
        required=True,
        label='Message:',
        widget=forms.Textarea(
            attrs={'class':'contact-form-textfield'})
        )