from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
    
class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)

    def serialize(self):
        return {
            "id": self.id,
            "username": self.user.username,
            "user_id": self.user.id,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "like": self.like,
        }

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="followers")
    followed = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="followed")

    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"


