from django.db import models

from course.models import Course, Lesson
from users.models import User

NULLABLE = {"blank": True, "null": True}

class Payments(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        help_text="Укажите пользователя",
        **NULLABLE,
    )
    payment_date = models.DateTimeField(
        verbose_name="Дата и время оплаты",
        help_text="Введите дату и время оплаты",
        **NULLABLE,
    )

    paid_course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Опалченный курс",
        help_text="Укажите оплаченный курс",
        **NULLABLE,
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        verbose_name="Опалченный урок",
        help_text="Укажите оплаченный урок",
        **NULLABLE,
    )

    payment_amount = models.PositiveIntegerField(
        verbose_name="Сумма оплаты", help_text="Введите сумму оплаты", **NULLABLE
    )

    payment_method = models.CharField(max_length=30,
        choices=[('cash', 'Наличными'), ('transfer', 'Перевод на счет')], verbose_name="Способ оплаты", **NULLABLE
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"Пользователь {self.user}({self.payment_method})"
