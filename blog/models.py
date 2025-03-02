from django.db import models          # Import Django's built-in database module

# Define a Blog Post model (This will create a database table)

class Post(models.Model):
    title = models.CharField(max_length=200)                # Title of the post (short text)
    content = models.TextField()                            # Content of the post (long text)
    created_at = models.DateTimeField(auto_now_add=True)    # Auto-filled timestamp

    # This method returns the title when querying objects in the Django shell
    def __str__(self):
        return self.title
