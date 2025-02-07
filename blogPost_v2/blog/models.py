from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name  
    

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    tags = models.ManyToManyField(Tag, related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="", null=False)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title

    def related_articles(self):
        return Article.objects.filter(tags__in=self.tags.all()).exclude(id=self.id).distinct()[:3]  # Limit to 3 related articles

    def latest_articles(self):
        return Article.objects.order_by('-created_at')[:3]  # Latest 3 articles


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author}'


class Contact(models.Model):
    Name = models.CharField(max_length=100)
    email =models.EmailField()
    subject=models.CharField(max_length=100)
    content =models.TextField()