from celery import shared_task
from django.core.mail import send_mail

from config import settings


@shared_task
def send_information_about_update_course(name, email):
    """Отправляет информацию об обновлении курса"""
    send_mail(
        f"Обновление курса!",
        f"Курс {name} обновлен.",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
