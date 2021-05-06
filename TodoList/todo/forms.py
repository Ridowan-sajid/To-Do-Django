from django import forms
from .models import Work
class TodoForm(forms.ModelForm):
    class Meta:
        model = Work
        fields=[
            'title',
            'date',
            'description'
        ]