# Generated by Django 5.1.1 on 2024-10-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0021_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_img',
            field=models.ImageField(upload_to='profile_images/'),
        ),
    ]
