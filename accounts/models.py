from django.db import models
from django.contrib.auth.models import User  

class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=5)  
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'The Name of reviewer: {self.user.username}'