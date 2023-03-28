from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class BlogPost(models.Model):
    post_title = models.CharField(max_length=70)
    post_content = models.TextField(max_length=10000)
    img = models.ImageField(
        upload_to="blog_images/",
        default="https://www.iforium.com/wp-content/uploads/Placeholder-Image-400.png",
        blank=True
    )

    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title
