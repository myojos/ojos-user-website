from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/register/', views.RegisterView.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
