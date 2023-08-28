from django.urls import path
from . import views

urlpatterns = [
    path('register_test/', views.registration_view, name='register'),
    path('register/', views.api_registration_view, name='register'),
    path('home/', views.HackathonDetailView.as_view(), name='hackathon-detail'),
    path('registration_success/', views.registration_success_view, name='registration_success'),
    path('export/', views.export_registered_students, name='export_registered_students'),
]

