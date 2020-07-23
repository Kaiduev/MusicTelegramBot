from django.db import models
from django_random_queryset import RandomManager


class Music(models.Model):
    name = models.CharField(max_length=255)
    audio = models.FileField(upload_to='musics/')

    objects = RandomManager()

    def __str__(self):
        return f"{self.name}"