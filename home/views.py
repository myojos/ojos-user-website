from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView

from .admin import OjosUserCreationForm

UserModel = get_user_model()


def index(request):
    return render(request, 'home/index.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is None:
        return HttpResponse('Activation link is invalid!')
    elif user.is_active:
        return HttpResponse('User is already active.')
    elif default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'registration/acc_active_complete.html')
    else:
        user.delete()
        return HttpResponse('Activation link expired, please sign up again.')


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = OjosUserCreationForm
    template_name = 'registration/registration.html'
    success_message = "You have successfully created an account!"

    # Display blank form
    def get(self, request, **kwargs):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'protocol': request.scheme,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'registration/verify.html')

        return render(request, self.template_name, {'form': form})
