from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from home.models import OjosUser
from .models import Camera, Event


class OjosUserUpdateForm(BSModalModelForm):
    class Meta:
        model = OjosUser
        fields = ['first_name', 'last_name']


class CameraCreateUpdateForm(BSModalModelForm):
    class Meta:
        model = Camera
        exclude = ['user', 'creation_date']
        labels = {
            'exit_door': 'This camera can see an exit door'
        }


class EventReportForm(BSModalModelForm):
    class Meta:
        model = Event
        fields = ['is_reported']


class GenerateReportForm(BSModalForm):
    day = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        fields = '__all__'

    def clean_day(self):
        data = self.cleaned_data['day']
        if data > timezone.now().date():
            raise ValidationError("Date cannot be in the future")
        return data
