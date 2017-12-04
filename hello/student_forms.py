from django import forms

class CandidateLogin(forms.Form):
    username = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255)