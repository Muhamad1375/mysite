from django.db import models

# Create your models here.
class Post(models.Model):
    #image
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tags
    #category
    #author
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    