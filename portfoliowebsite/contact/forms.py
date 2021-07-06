from django import forms

class ContactForm(forms.Form):
    from_name = forms.CharField(
        required=True,
        label='Your Name:',
        widget=forms.TextInput(
            attrs={'class':'form-textfield'}
        ))
    from_email = forms.EmailField(
        required=True,
        label='Your Email:', 
        error_messages = {'Invalid Email': 'Please enter a valid email.'},
        widget=forms.TextInput(
            attrs={'class':'form-textfield'})
        )
    subject = forms.CharField(
        required=True,
        label='Subject:',
        widget=forms.TextInput(
            attrs={'class':'form-textfield'})
        )
    contact_message = forms.CharField(
        required=True,
        label='Message:',
        widget=forms.Textarea(
            attrs={'class':'form-textfield'})
        )
