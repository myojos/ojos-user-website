from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Event, User


def index(request):
    return HttpResponseRedirect(reverse('app:profile'))


class ProfileUpdate(generic.edit.UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'phone']
    template_name = 'app/profile.html'

    def get_object(self, **kwargs):
        return User.objects.get(pk=1)

    def get_success_url(self):
        return reverse_lazy('app:profile')


class EventsView(generic.ListView):
    model = Event
    template_name = 'app/events.html'
    context_object_name = 'user_events'
    paginate_by = 10
    queryset = Event.objects.filter(user=1).order_by('-timestamp')


def events(request, page=1):
    user_events = Event.objects
    context = {'user_events': user_events}
    return render(request, 'app/events.html', context)
