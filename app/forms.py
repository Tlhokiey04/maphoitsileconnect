from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Issue, Profile

class IssueForm(forms.ModelForm):
    class Meta:
        model  = Issue
        fields = ['title', 'category', 'description', 'location', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class':       'form-control',
                'placeholder': 'Brief title e.g. Water leak on Moshoeshoe St',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class':       'form-control',
                'rows':        4,
                'placeholder': 'Describe the issue in detail...',
            }),
            'location': forms.TextInput(attrs={
                'class':       'form-control',
                'placeholder': 'Street address or nearest landmark',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }


class RegisterForm(UserCreationForm):
    email        = forms.EmailField(required=True)
    first_name   = forms.CharField(max_length=50)
    last_name    = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=20, required=False)
    suburb       = forms.CharField(max_length=100, required=False)

    class Meta:
        model  = User
        fields = [
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user            = super().save(commit=False)
        user.email      = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name  = self.cleaned_data['last_name']
        if commit:
            user.save()
            user.profile.phone_number = self.cleaned_data.get('phone_number', '')
            user.profile.suburb       = self.cleaned_data.get('suburb', '')
            user.profile.save()
        return user