from django.urls import path
from .views import post_list, create_post, register, user_login, user_logout, post_detail, like_post  # Corrected import

urlpatterns = [
    path('', post_list, name='post_list'),  # Map the root URL to the post_list view
    path('new/', create_post, name='create_post'),  # Page to create new posts
    path('register/', register, name='register'),  # User registration
    path('login/', user_login, name='login'),  # User login
    path('logout/', user_logout, name='logout'),  # User logout
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', like_post, name='like_post'),

]
