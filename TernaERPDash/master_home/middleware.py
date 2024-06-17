# middleware.py
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.contrib import messages

@receiver(user_logged_out)
def handle_logout(sender, user, request, **kwargs):
    messages.success(request, "You have been logged out due to inactivity.")

user_logged_out.connect(handle_logout)