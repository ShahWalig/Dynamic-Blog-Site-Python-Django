# Generated by Django 5.1.1 on 2024-10-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0011_profiletesting_description_profiletesting_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_like',
            field=models.IntegerField(default=0),
        ),
    ]
