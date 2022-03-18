from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    slag = models.CharField(max_length=20)
    description = models.TextField()
    datetime = models.DateTimeField()
    url_source = models.URLField(max_length=100)
    image = models.FilePathField(path="/img")


