from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    ARTICLE = 'article'
    BLOG = 'blog'
    PODCAST = 'podcast'
    TYPE_CHOICES = [
        (ARTICLE, 'Article'),
        (BLOG, 'Blog'),
        (PODCAST, 'Podcast'),
    ]
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    description = models.TextField(blank=True)
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default=ARTICLE,
    )

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    excerpt = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    categories = models.ManyToManyField(Category, related_name='posts')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"