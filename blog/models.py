from django.db import models          # Import Django's built-in database module
from django.contrib.auth.models import User

# Define a Blog Post model (This will create a database table)

class Post(models.Model):
    title = models.CharField(max_length=200)                # Title of the post (short text)
    content = models.TextField()                            # Content of the post (long text)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Add default value
    created_at = models.DateTimeField(auto_now_add=True)    # Auto-filled timestamp
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)


    # This method returns the title when querying objects in the Django shell
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
