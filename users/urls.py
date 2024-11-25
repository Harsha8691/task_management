from django.urls import path
from .views import register_with_invitation

urlpatterns = [
    path('register/<uuid:token>/', register_with_invitation, name='register_with_invitation'),
]
