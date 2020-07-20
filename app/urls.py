from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('events', views.EventsView.as_view(), name='events'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('update_profile/<int:pk>', views.UserUpdateView.as_view(), name='update_profile'),
    path('add_camera', views.CameraCreateView.as_view(), name='add_camera'),
    path('update/<int:pk>', views.CameraUpdateView.as_view(), name='update_camera'),
    path('delete/<int:pk>', views.CameraDeleteView.as_view(), name='delete_camera'),
    path('report/<int:pk>', views.EventReportView.as_view(), name='report_event'),
    path('generate/', views.GenerateReportView.as_view(), name='generate_report'),
]
