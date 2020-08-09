from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from .models import Camera, Event


class CameraAdmin(admin.ModelAdmin):
    list_display = ('email', 'location', 'app', 'creation_date')

    def email(self, obj):
        return obj.user.email

    list_filter = (('creation_date', DateRangeFilter),)
    search_fields = ('user__email',)
    ordering = ('user__email', '-creation_date')


class EventAdmin(admin.ModelAdmin):
    list_display = ('email', 'event_type', 'video_link', 'timestamp', 'is_reported', 'is_visible')

    def email(self, obj):
        return obj.camera.user.email

    list_filter = (('timestamp', DateRangeFilter), 'is_reported', 'is_visible')
    search_fields = ('camera__user__email', 'timestamp')
    ordering = ('camera__user__email', '-timestamp')


admin.site.register(Camera, CameraAdmin)
admin.site.register(Event, EventAdmin)
