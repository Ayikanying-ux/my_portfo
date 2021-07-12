
from django import forms
import re

def validate_message_count(value):
    count = len(value.split())
    if count < 20:
        raise forms.ValidationError('Please provide a 20 message word')

class ContactForm(forms.Form):
    Firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter first name', 'style': 'width: 100%;', 'class': 'form-control'}))
    Lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter last name', 'style': 'width: 100%;', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 100%;', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 100%;', 'class': 'form-control'}), validators=[validate_message_count])

    def __init__(self, *args, **kwargs):
        initial_arguments = kwargs.get('initial', None)
        updated_initial = {}
        if initial_arguments:
            user = initial_arguments.get('user', None)
            if user:
                updated_initial["Firstname"] = getattr(user, 'Firstname', None)
                updated_initial['Lastname'] = getattr(user, 'Lastname', None)
                updated_initial['email'] = getattr(user, 'email', None)

        updated_initial['message'] = "Please enter a message"
        kwargs.update(initial=updated_initial)
        super(ContactForm, self).__init__(*args, **kwargs)