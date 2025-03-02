from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from .forms import PostForm, RegisterForm

# View function to display all blog posts

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign post to logged-in user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('post_list')  # Redirect to home page
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('post_list')  # Redirect to home page
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

# User Logout View
def user_logout(request):
    logout(request)
    return redirect('post_list')  # Redirect to home page after logout