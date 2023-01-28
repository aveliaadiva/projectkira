from django.db import models

from embed_video.fields import EmbedVideoField

class Video(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=200)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-added']