from django.db import models


# App model is defined here.
class Story(models.Model):
    story_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=100)
    title = models.TextField()
    url = models.URLField(null=True, blank=True)
    score = models.IntegerField(default=0)
    sentiment = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
