from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# on_delete=models.CASCADE
# on_delete=models.SET_NULL
# on_delete=models.DO_NOTHING
# on_delete=models.PROTECT


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
