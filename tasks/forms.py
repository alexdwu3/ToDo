from .models import *
from django import forms
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task # creating form for "task" model
        fields = '__all__' # all fields allowed