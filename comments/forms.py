from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'body')

        def clean(self):
            data = self.cleaned_data
            if data.get('email', None) or data.get('body', None):
                return data
