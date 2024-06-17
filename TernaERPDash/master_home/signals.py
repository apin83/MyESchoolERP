# signals.py
from django.db.models.signals import session_expired
# from django.contrib.sessions.middleware import session_expired
from django.dispatch import receiver

@receiver(session_expired)
def handle_session_expired(sender, session_key, **kwargs):
    # Add your custom logic here
    print(f"Session expired for session key: {session_key}")

session_expired.connect(handle_session_expired)