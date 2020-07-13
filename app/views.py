from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from home.models import User
from .models import Event


def index(request):
    return HttpResponseRedirect(reverse('app:profile'))


class ProfileUpdate(generic.edit.UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'phone']
    template_name = 'app/profile.html'

    def get_object(self, **kwargs):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('app:profile')


class EventsView(generic.ListView):
    model = Event
    template_name = 'app/events.html'
    context_object_name = 'user_events'
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user).order_by('-timestamp')


def events(request):
    user_events = Event.objects
    context = {'user_events': user_events}
    return render(request, 'app/events.html', context)
