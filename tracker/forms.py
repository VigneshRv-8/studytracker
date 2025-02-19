from django import forms
from .models import Topic

class TopicForm(forms.Form):
    subject = forms.CharField(max_length=100)
    topics = forms.CharField(widget=forms.Textarea, help_text="Enter topics separated by commas")
