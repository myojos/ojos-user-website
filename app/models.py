from django.conf import settings
from django.db import models
from django.db.models.functions import Now
from django.utils import timezone
from django.core.validators import MaxValueValidator

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

    def __str__(self):
        return f"{self.user.email} - {self.location}".lower()

    def get_location(self):
        return self.location.replace('_', ' ').capitalize()


class Event(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=200)
    timestamp = models.DateTimeField('Timestamp', validators=[MaxValueValidator(limit_value=timezone.now)])
    video_link = models.URLField()
    is_reported = models.BooleanField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(timestamp__lte=Now()),
                name='event_timestamp_cannot_be_future_dated'
            )
        ]

    def __str__(self):
        return self.event_type

    def is_old(self):
        return (timezone.now() - self.timestamp).days >= 14
