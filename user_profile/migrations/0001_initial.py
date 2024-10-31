# Generated by Django 5.1.1 on 2024-10-07 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('user_img', models.ImageField(blank=True, upload_to='profile_images/')),
                ('joined_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]