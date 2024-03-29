from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# tags
from taggit.managers import TaggableManager
# markdown
from markdownx.models import MarkdownxField
# slug
from django.utils.text import slugify
# users
# from django.contrib.auth.models import User

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = ( ('draft', 'Draft'), ('published', 'Published'),)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # body = models.TextField()
    body = MarkdownxField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() # the default manager.
    published = PublishedManager() # Our custom manager.
    tags = TaggableManager()

    def save(self, *args, **kwargs):
        # Generate the slug from the title if it's not provided
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
    

    def get_absolute_url(self):
        return reverse("blog:post_detail", 
                        args=[self.publish.year, self.publish.month, self.publish.day, self.slug])




    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    retrieve the post of a comment object using comment.post and retrieve all
    comments of a post using post.comments.all()
    """
    post = models.ForeignKey(Post,
        on_delete=models.CASCADE,
        related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'