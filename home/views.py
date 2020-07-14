from django.contrib.auth import login, authenticate
from django.contrib.auth.password_validation import validate_password
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .admin import UserCreationForm


def index(request):
    return render(request, 'home/index.html')


def contact(request):
    return render(request, 'home/contact-us.html')


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'
    success_message = "You have successfully created an account!"

    # Display blank form
    def get(self, request, **kwargs):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)  # Do not save to table yet
            password = form.cleaned_data['password1']

            try:
                validate_password(password, user)
            except ValidationError as e:
                form.add_error('password1', e)  # to be displayed with the field's errors
                return render(request, self.template_name, {'form': form})

            # Login the user and redirect
            user = form.save()
            login(request, user)
            return redirect('app:index')

        return render(request, self.template_name, {'form': form})
