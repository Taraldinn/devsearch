import uuid

from cloudinary.models import CloudinaryField
from django.db import models


# Create your models here.
from tinymce.models import HTMLField


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField(null=True, blank=True)
    featured_image = CloudinaryField('image', folder='aldinn/devconnects/featuredImage/')
    demo_link = models.URLField(null=True, blank=True, max_length=2000)
    source_link = models.URLField(null=True, blank=True, max_length=2000)
    tags = models.ManyToManyField("Tag", blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        {'up', 'Up Vote'},
        {'down', 'Down Vote'},
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(choices=VOTE_TYPE, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    def __str__(self):
        return self.name
