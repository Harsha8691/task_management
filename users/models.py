from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.utils.timezone import now

class User(AbstractUser):
    """
    Custom User model extending AbstractUser.
    """
    def __str__(self):
        return self.username


class Invitation(models.Model):
    """
    Model for handling user invitations.
    """
    email = models.EmailField(unique=True)  # Email of the invitee
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)  # Unique invitation token
    created_at = models.DateTimeField(auto_now_add=True)  # When the invitation was created
    expires_at = models.DateTimeField()  # Expiry time for the invitation
    used = models.BooleanField(default=False)  # Whether the invitation has been used

    def is_expired(self):
        """
        Check if the invitation token has expired.
        """
        return now() > self.expires_at

    def __str__(self):
        return f"Invitation for {self.email}"
