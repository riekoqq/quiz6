from django.db import models
from account.models import User

# Create your models here.
class Post(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Content = models.TextField()
    Created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Content

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Report by {self.user.username} on {self.post} - {self.message}'

