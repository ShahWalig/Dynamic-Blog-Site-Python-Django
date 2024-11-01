# Generated by Django 5.1.1 on 2024-10-14 07:21

import ckeditor.fields
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0024_alter_profile_user_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_update_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
