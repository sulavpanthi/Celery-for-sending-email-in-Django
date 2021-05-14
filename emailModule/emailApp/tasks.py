from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_email_to_all(receiver_list):
    subject = "Test Message"
    message = "Hello World"
    send_mail(subject=subject, message = message, from_email = settings.EMAIL_HOST_USER,
     recipient_list = receiver_list, fail_silently = False)
    return None
