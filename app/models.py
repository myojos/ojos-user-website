from django.conf import settings
from django.db import models


class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    timestamp = models.DateTimeField('Timestamp')
    video_link = models.CharField(max_length=300)

    def __str__(self):
        return self.event_type
