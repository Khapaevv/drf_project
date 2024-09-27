from django.db import models

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
    video = models.FileField(
        upload_to="course/videos",
        verbose_name="Видео",
        help_text="Загрузите видео",
        **NULLABLE,
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Курс", **NULLABLE
    )

    def __str__(self):
        return f"Тема урока {self.name}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
