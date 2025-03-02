from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post # Use the post model
        fields = ['title', 'content']

# User Registration Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add an email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Fields to display