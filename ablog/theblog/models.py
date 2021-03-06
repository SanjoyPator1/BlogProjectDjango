from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Privacy(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    # header_image = models.ImageField(
    #     null=True, blank=True, upload_to="images/")
    # title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    body = models.TextField(blank=True, null=True)

    # body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='all')
    privacy = models.CharField(max_length=255, default='private')
    checkpublic = models.CharField(max_length=255, default='public')
    snippet = models.CharField(
        max_length=255)

    likes = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return str(self.title) + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

    def total_likes(self):
        return self.likes.count()


#summernote rty

class Post1(models.Model):
    title = models.CharField(max_length=255, help_text="Title of blog posting")
    body = models.TextField(blank=True, null=True)


class Author(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField(blank=True, null=True)
