from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Invitation

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Customized UserAdmin for managing User objects in the admin interface.
    """
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)
    fieldsets = UserAdmin.fieldsets


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    """
    Admin panel for managing Invitation objects.
    """
    list_display = ('email', 'token', 'created_at', 'expires_at', 'used')  
    list_filter = ('used', 'expires_at')  
    search_fields = ('email', 'token')  
    actions = ['resend_invitation']

    def resend_invitation(self, request, queryset):
        """
        Custom admin action to resend selected invitations.
        """
        for invitation in queryset:
            if not invitation.is_expired():
                # Logic to resend the invitation email goes here
                self.message_user(request, f"Resent invitation to {invitation.email}")
            else:
                self.message_user(
                    request,
                    f"Cannot resend invitation to {invitation.email}. The token is expired.",
                    level='error'
                )
    resend_invitation.short_description = "Resend selected invitations"
