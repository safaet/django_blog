from django.urls import path
from .views import post_list, create_post  # Import our view function

urlpatterns = [
    path('', post_list, name='post_list'),  # Map the root URL to the post_list view
    path('new/', create_post, name='create_post'),  # Page to create new posts

]
