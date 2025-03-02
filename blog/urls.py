from django.urls import path
from .views import post_list  # Import our view function

urlpatterns = [
    path('', post_list, name='post_list'),  # Map the root URL to the post_list view
]
