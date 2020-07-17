from contact_form.views import ContactFormView
from django.conf import settings
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from django.views.generic import TemplateView

from . import views
from .forms import EmailValidationOnForgotPassword

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', ContactFormView.as_view(
        recipient_list=[settings.EMAIL_HOST_USER],
        success_url=reverse_lazy('home:contact_form_sent')
    ), name='contact_form'),
    path('contact/sent/', TemplateView.as_view(template_name='contact_form/contact_form_sent.html'), name='contact_form_sent'),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        form_class=EmailValidationOnForgotPassword,
        success_url=reverse_lazy('home:password_reset_done')
    ), name='password_reset'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('home:password_reset_complete')
    ), name='password_reset_confirm'),
    path('accounts/register/', views.RegisterView.as_view(), name='register'),
    path('accounts/activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('accounts/', include('django.contrib.auth.urls')),
]
