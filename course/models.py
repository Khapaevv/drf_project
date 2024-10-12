from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование курса",
        help_text="Введите наименование курса",
    )
    preview = models.ImageField(
        upload_to="course/previews",
        verbose_name="Картинка",
        help_text="Загрузите картинку",
        **NULLABLE,
    )
    description = models.TextField(
        verbose_name="Описание курса",
        help_text="Введите описание курса",
        **NULLABLE,
    )
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Владелец"
    )

    def __str__(self):
        def __str__(self):
            return f"Название курса {self.name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование урока",
        help_text="Введите наименование урока",
    )
    description = models.TextField(
        verbose_name="Описание урока",
        help_text="Введите описание урока",
        **NULLABLE,
    )
    preview = models.ImageField(
        upload_to="course/previews",
        verbose_name="Картинка",
        help_text="Загрузите картинку",
        **NULLABLE,
    )

    video = models.URLField(
        max_length=200, verbose_name="Ссылка на видео", **NULLABLE,
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Курс", **NULLABLE
    )
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Владелец"
    )

    def __str__(self):
        return f"Тема урока {self.name}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
