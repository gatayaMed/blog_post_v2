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
