from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .admin import UserCreationForm


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def register(request):
    if request.method == "GET":
        return render(
            request, "registration/registration.html",
            {"form": UserCreationForm}
        )
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse('congrats')

        else:
            return render(request, 'registration/registration.html', {'form': form})
