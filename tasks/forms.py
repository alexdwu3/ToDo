from .models import *
from django import forms
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = Task # creating form for "task" model
        fields = '__all__' # all fields allowed