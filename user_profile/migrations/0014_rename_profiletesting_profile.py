# Generated by Django 5.1.1 on 2024-10-12 15:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0013_delete_profile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileTesting',
            new_name='Profile',
        ),
    ]
