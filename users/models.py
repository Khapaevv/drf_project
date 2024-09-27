from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):

    username = None

    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Введите email"
    )
    phone = models.CharField(
        max_length=15, verbose_name="Телефон", help_text="Укажите телефон", **NULLABLE
    )
    city = models.CharField(
        max_length=50, verbose_name="Город", help_text="Укажите город", **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватарка",
        help_text="Загрузите аватарку",
        **NULLABLE,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("email",)

    def __str__(self):
        return f"Пользователь {self.email}({self.name})"
