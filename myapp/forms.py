from django import forms
from django.forms import fields
from .models import student

class studentform(forms.ModelForm):
    class Meta:
        model= student
        fields="__all__"
        


