from django.shortcuts import render
from .models import Post

# View function to display all blog posts

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})