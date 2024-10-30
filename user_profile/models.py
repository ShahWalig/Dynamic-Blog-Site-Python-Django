from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField  # Import CKEditor RichTextField


class Profile(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    age = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    joined_date = models.DateField(blank=True, null=True)
    user_img = models.ImageField(upload_to='profile_images/', default='profile_images/default.png')


    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    def __str__(self):
        return self.user.username


class Post(models.Model):
    post_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=200, blank=True)
    post_like = models.ManyToManyField(User, related_name='blog_posts_likes')
    post_comment = models.CharField(max_length=200, blank=True)
    post_title = models.CharField(max_length=200, blank=True)
    post_description = RichTextField(blank=True)
    post_img = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def total_likes(self):
        return self.post_like.count()

    def __str__(self):
        return self.post_owner.username


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="post_comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.post_title}'
