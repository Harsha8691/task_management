from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Invitation

def register_with_invitation(request, token):
    invitation = get_object_or_404(Invitation, token=token, used=False)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = invitation.email
            user.save()
            invitation.used = True
            invitation.save()
            return HttpResponse("Registration successful!")
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
