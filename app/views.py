from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from home.models import User
from .models import Event


@login_required
def index(request):
    return HttpResponseRedirect(reverse('app:profile'))


class ProfileUpdate(LoginRequiredMixin, generic.edit.UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'phone']
    template_name = 'app/profile.html'

    def get_object(self, **kwargs):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('app:profile')


class EventsView(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'app/events.html'
    context_object_name = 'user_events'
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user).order_by('-timestamp')
