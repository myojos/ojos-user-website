from django.db import models
from django.shortcuts import reverse
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    creation_date = models.DateTimeField('Creation date')
    email = models.EmailField()
    phone = PhoneNumberField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('app:profile', args=(self.id,))


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    timestamp = models.DateTimeField('Timestamp')
    video_link = models.CharField(max_length=300)

    def __str__(self):
        return self.event_type
