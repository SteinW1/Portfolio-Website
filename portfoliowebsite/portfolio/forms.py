from django import forms

class ContactForm(forms.Form):
    from_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-textfield'}
        ))
    from_email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class':'form-textfield'}
        ))
    subject = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class':'form-textfield'}
        ))
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class':'form-textfield'}
        ))