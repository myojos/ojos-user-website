from django.conf import settings
from django.db import models
from django.utils import timezone


class Camera(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now())

    class App(models.TextChoices):
        XIAOMI = 'XIAOMI', 'Xiaomi'
        LITTLELF = 'LITTLELF', 'Littlelf'
        ICSEE = 'ICSEE', 'iCSee'
        HIK = 'HIKCONNECT', 'Hik-Connect'

    app = models.CharField(max_length=20, choices=App.choices)
    auth_key = models.CharField(max_length=20)
    auth_pass = models.CharField(max_length=20)

    class Location(models.TextChoices):
        BEDROOM = 'BEDROOM', 'Bedroom'
        KITCHEN = 'KITCHEN', 'Kitchen'
        LIVING_ROOM = 'LIVING_ROOM', 'Living Room'

    location = models.CharField(max_length=20, choices=Location.choices)
    exit_door = models.BooleanField()


class Event(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    timestamp = models.DateTimeField('Timestamp')
    video_link = models.URLField()
    is_reported = models.BooleanField()

    def __str__(self):
        return self.event_type

    def is_old(self):
        return (timezone.now() - self.timestamp).days >= 14
