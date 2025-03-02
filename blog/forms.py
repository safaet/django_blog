from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post # Use the post model
        fields = ['title', 'content']