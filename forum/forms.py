from django import forms
from .models import Thread


class PostForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ('title', 'content')
