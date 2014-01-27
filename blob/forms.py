# forms.py
from django import forms

class TextForm(forms.Form):
    datext  = forms.CharField()
