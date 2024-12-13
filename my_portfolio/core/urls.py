from django.urls import path

from . import views

urlpatterns = [
    path('api/contact-form/', views.receive_contact_from_api, name='contact-form'),
]