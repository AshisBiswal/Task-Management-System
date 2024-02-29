from django import forms
from .models import taskmodel,Comment


class loginform(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class registerform(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

class taskform(forms.ModelForm):
    class Meta:
        model = taskmodel
        fields = "__all__"
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})  # Specify the widget for the due_date field
        }


class commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

