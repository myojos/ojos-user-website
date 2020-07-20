from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from home.models import OjosUser
from .forms import OjosUserUpdateForm, CameraCreateUpdateForm, EventReportForm
from .models import Event, Camera


@login_required
def index(request):
    return HttpResponseRedirect(reverse_lazy('app:profile'))


class ProfileView(LoginRequiredMixin, generic.ListView):
    model = Camera
    context_object_name = 'user_cameras'
    template_name = 'app/profile.html'

    def get_queryset(self):
        return Camera.objects.filter(user=self.request.user).order_by('creation_date')


class UserUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = OjosUser
    template_name = 'app/update_user_form.html'
    form_class = OjosUserUpdateForm
    success_message = 'Your information was updated.'
    success_url = reverse_lazy('app:profile')


class CameraCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'app/add_camera_form.html'
    form_class = CameraCreateUpdateForm
    success_message = 'Camera was created.'
    success_url = reverse_lazy('app:profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CameraUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Camera
    template_name = 'app/update_camera_form.html'
    form_class = CameraCreateUpdateForm
    success_message = 'Camera was updated.'
    success_url = reverse_lazy('app:profile')


class CameraDeleteView(BSModalDeleteView):
    model = Camera
    template_name = 'app/delete_camera_form.html'
    success_message = 'Camera was deleted.'
    success_url = reverse_lazy('app:profile')


class EventsView(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'app/events.html'
    context_object_name = 'user_events'
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.filter(camera__user=self.request.user).order_by('-timestamp')


class EventReportView(BSModalUpdateView):
    model = Event
    template_name = 'app/report_event_form.html'
    form_class = EventReportForm
    success_message = 'Thank you for helping us improve! The event was reported successfully and our team will get on it shortly.'
    success_url = reverse_lazy('app:events')

    def form_valid(self, form):
        form.instance.is_reported = True
        return super().form_valid(form)
