# Generated by Django 5.1.1 on 2024-10-13 03:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0017_remove_post_post_title_post_post_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_like',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_title',
        ),
        migrations.AddField(
            model_name='post',
            name='post_like',
            field=models.ManyToManyField(related_name='blog_posts_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='post_title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
