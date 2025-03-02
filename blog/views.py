from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

from django.contrib.auth.forms import AuthenticationForm
from .forms import PostForm, RegisterForm

from django.http import JsonResponse

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

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()  # Get all comments for the post
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)  # Unlike
        liked = False
    else:
        post.likes.add(request.user)  # Like
        liked = True

    return JsonResponse({'liked': liked, 'total_likes': post.total_likes()})