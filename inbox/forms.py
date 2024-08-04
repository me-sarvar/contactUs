from django import forms
from .models import Messages


class ContactForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('first_name', 'last_name', 'email', 'message')

        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'max-width: 300px;', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'max-width: 300px;', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'style': 'max-width: 300px;', 'placeholder': 'Email'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'style': 'max-width: 300px;', 'placeholder': 'Your message'}),
        }

class AddSpamWordsForm(forms.Form):
    spam_words = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple())