from bootstrap_modal_forms.forms import BSModalModelForm

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
