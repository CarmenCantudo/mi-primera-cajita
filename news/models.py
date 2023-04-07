from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class News(models.Model):
    """
    News Articles Model
    """
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='news')
    content = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='news/', max_length=1024,
                              null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Orders the News in Descending order
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string method "AKA :The Magic method""
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        Generate unique slug
        """
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Comments Model
    """
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80, unique=True)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order the comments in ascending order (oldest first)
        """
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
