from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=20)
    parent = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title



class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    body = models.TextField()
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.SET_NULL, null=True)
    caption = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=150, blank=True)
    keywords = ArrayField(models.CharField(max_length=10, blank=True),null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    main_image = models.ImageField(upload_to="main_image", blank=True, null=True)
    header_image = models.ImageField(upload_to="header_image", blank=True, null=True)





    def __str__(self):
        return self.title