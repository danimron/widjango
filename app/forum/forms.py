from django import forms
from .models import Thread


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Judul'
        self.fields['title'].widget.attrs['class'] = 'form-control mb-2'

    class Meta:
        model = Thread
        fields = ('title', 'content')
