# images/models.py

from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    image_base64 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
