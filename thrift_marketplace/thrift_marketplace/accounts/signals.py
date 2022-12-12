from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags


UserModel = get_user_model()


@receiver(signal=post_save, sender=UserModel)
def send_greeting_email(instance, created, **kwargs):
    if created:
        subject = 'Welcome to Thrift Marketplace'
        html_message = render_to_string('accounts/email-greeting.html', {
            'user': instance.username,
        })
        email_content = strip_tags(html_message)
        send_mail(
            subject=subject,
            message=email_content,
            html_message=html_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=(instance.email,),
        )




